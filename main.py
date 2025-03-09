import os
import datetime
import logging
from docker import DockerClient
from kubernetes import client, config
from kubernetes.client.rest import ApiException

class DeploymentAutomation:
    """
    A class used to automate the deployment of applications using Docker and Kubernetes.

    ...

    Attributes
    ----------
    docker_client : DockerClient
        a DockerClient object to interact with Docker
    k8s_client : ApiClient
        a Kubernetes ApiClient object to interact with Kubernetes
    namespace : str
        the namespace in Kubernetes where the deployment will take place
    docker_username : str
        the username to authenticate with Docker
    docker_password : str
        the password to authenticate with Docker
    docker_registry : str
        the Docker registry where the application's Docker image is stored

    Methods
    -------
    deploy_application(app_name: str, deployment_config_path: str) -> None:
        Deploys the application to Kubernetes.
    """

    def __init__(self, namespace: str, docker_registry: str):
        """
        Constructs all the necessary attributes for the DeploymentAutomation object.

        Parameters
        ----------
            namespace : str
                the namespace in Kubernetes where the deployment will take place
            docker_registry : str
                the Docker registry where the application's Docker image is stored
        """

        self.docker_client = DockerClient.from_env()
        self.k8s_client = None
        self.namespace = namespace
        self.docker_username = os.getenv('DOCKER_USERNAME')
        self.docker_password = os.getenv('DOCKER_PASSWORD')
        self.docker_registry = docker_registry

        # Configure logging
        logging.basicConfig(filename='deployment.log', level=logging.INFO)

        # Load Kubernetes configuration
        try:
            config.load_kube_config()
            self.k8s_client = client.AppsV1Api()
        except Exception as e:
            logging.error(f"Failed to load Kubernetes configuration: {str(e)}")
            raise

    def deploy_application(self, app_name: str, deployment_config_path: str) -> None:
        """
        Deploys the application to Kubernetes.

        Parameters
        ----------
            app_name : str
                the name of the application to be deployed
            deployment_config_path : str
                the path to the Kubernetes deployment configuration file
        """

        try:
            # Pull the latest version of the application from the Docker registry
            self.docker_client.images.pull(self.docker_registry, tag='latest')

            # Create a new Docker image of the application, tagging it with the current timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            image = self.docker_client.images.build(path='.', tag=f"{self.docker_registry}:{timestamp}")
            image.tag(self.docker_registry, tag=timestamp)

            # Push this new Docker image to the Docker registry
            self.docker_client.images.push(self.docker_registry, tag=timestamp)

            # Update the Kubernetes deployment configuration to use this new Docker image
            with open(deployment_config_path) as file:
                dep = yaml.safe_load(file)
                dep['spec']['template']['spec']['containers'][0]['image'] = f"{self.docker_registry}:{timestamp}"

            # Apply the updated Kubernetes configuration to the cluster
            resp = self.k8s_client.patch_namespaced_deployment(
                name=app_name,
                namespace=self.namespace,
                body=dep
            )

            # Monitor the status of the deployment
            while True:
                resp = self.k8s_client.read_namespaced_deployment(name=app_name, namespace=self.namespace)
                if resp.status.ready_replicas == resp.status.replicas:
                    break

        except ApiException as e:
            logging.error(f"Exception when calling Kubernetes API: {str(e)}")
            # Rollback the deployment to the previous stable version
            self.k8s_client.create_namespaced_deployment_rollback(name=app_name, namespace=self.namespace)
            raise
        except Exception as e:
            logging.error(f"Failed to deploy application: {str(e)}")
            raise