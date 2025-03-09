import unittest
from unittest.mock import patch, Mock
from main import DeploymentAutomation

class TestDeploymentAutomation(unittest.TestCase):

    @patch('main.DockerClient')
    @patch('main.client.AppsV1Api')
    def setUp(self, mock_k8s_client, mock_docker_client):
        self.deployer = DeploymentAutomation('my-namespace', 'my-docker-registry')
        self.deployer.docker_client = mock_docker_client
        self.deployer.k8s_client = mock_k8s_client

    def test_deploy_application(self):
        self.deployer.deploy_application('my-app', 'path/to/deployment.yaml')
        self.deployer.docker_client.images.pull.assert_called_with('my-docker-registry', tag='latest')
        self.deployer.k8s_client.patch_namespaced_deployment.assert_called()

if __name__ == '__main__':
    unittest.main()