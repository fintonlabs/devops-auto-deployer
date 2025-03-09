# An automation script that deploys applications across different environments using Docker and Kubernetes, with the ability to rollback if necessary


## Table of Contents

- [📋 Table of Contents](#📋-table-of-contents)
- [Prerequisites](#prerequisites)
- [Step-by-step Installation Process](#step-by-step-installation-process)
- [Verification Steps](#verification-steps)
- [Post-Installation Configuration](#post-installation-configuration)
- [Prerequisites](#prerequisites)
- [1. Basic Usage](#1.-basic-usage)
- [2. Common Use Cases](#2.-common-use-cases)
- [3. Command-line Arguments](#3.-command-line-arguments)
- [4. Expected Output](#4.-expected-output)
- [5. Advanced Usage](#5.-advanced-usage)
- [Class Description](#class-description)
- [Attributes](#attributes)
- [Methods](#methods)
- [Example](#example)
- [Common Patterns and Best Practices](#common-patterns-and-best-practices)
- [⚙️ Configuration](#⚙️-configuration)
- [🔍 Troubleshooting](#🔍-troubleshooting)
- [🤝 Contributing](#🤝-contributing)
- [📄 License](#📄-license)
- [Features](#features)
- [API Documentation](#api-documentation)
# Project Overview

This project is a Python based automation script designed to streamline the deployment of applications across different environments using Docker and Kubernetes. The objective of the project is to automate the often complex and time-consuming process of deploying applications, allowing for a smoother and more efficient deployment process. The script also includes the capability to rollback the deployment if necessary, thereby adding an additional layer of security and reliability to your application deployment process.

# Features :sparkles:

The following are the key features of the Deployment Automation script:

- **Docker Interaction** 🐳: Using the `DockerClient` object from the Docker Python SDK, the script is able to interact with Docker. This includes tasks such as creating Docker images, starting and managing Docker containers, and interacting with Docker registries.

- **Kubernetes Interaction** ☸️: With the help of the `ApiClient` object from the Kubernetes Python client, the script is able to manage deployments on a Kubernetes cluster. This includes operations such as creating deployments, managing services, and handling pods.

- **Namespace Specific Deployments** 🔖: The script allows deployments to be made in a specific Kubernetes namespace. This can be useful when managing deployments in complex environments where multiple teams or projects are using the same Kubernetes cluster.

- **Docker Authentication** 🔐: The script contains the ability to authenticate with Docker using a username and password. This is vital when interacting with private Docker registries.

- **Application Deployment** 🚀: One of the key features of the script is the `deploy_application` method. This method deploys an application to a Kubernetes cluster by taking in the application's name and the path to the deployment configuration file as parameters.

- **Rollback Mechanism** ⏮️: In case of any issues with the deployment, the script includes a rollback mechanism. This allows you to revert your application to its previous state, thereby reducing potential downtime and ensuring the stability of your application.

- **Logging** 📝: The script utilizes Python's `logging` module to keep track of the various operations being performed. This can be invaluable when debugging issues or tracking the progress of deployments.

- **Environment Variables** 🌍: The script makes use of environment variables to store sensitive information, such as the Docker username and password. This helps to keep your sensitive data secure and separated from your codebase.

These features collectively make the Deployment Automation script a robust and reliable tool for managing your application deployments. It not only simplifies the deployment process but also ensures that your applications are deployed in a secure and controlled manner.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Installation Guide

In this guide, we will walk through the steps to install and run the DeploymentAutomation script. This script allows automated deployment of applications using Docker and Kubernetes with rollback capability.

## Prerequisites

Before starting the installation process, ensure the following prerequisites are met:

1. **Python**: The script is written in Python. Make sure you have Python 3.6 or higher installed on your system. You can download Python from [here](https://www.python.org/downloads/).

2. **Docker**: You need to have Docker installed on your system. If not, you can download it from [here](https://www.docker.com/products/docker-desktop).

3. **Kubernetes**: You should have a working Kubernetes environment. If not, you can set it up using [MiniKube](https://minikube.sigs.k8s.io/docs/start/).

4. **Python Modules**: The script uses some Python modules. You can install these modules using pip (Python’s package manager).

## Step-by-step Installation Process

Follow these steps to install the DeploymentAutomation script:

1. **Clone the Repository**

    First, clone the repository that contains the script. Open your terminal and use the git clone command:

    ```bash
    git clone https://github.com/your_repository_url.git
    ```

2. **Navigate to the Directory**

    Navigate to the directory that contains the script:

    ```bash
    cd path_to_directory
    ```

3. **Install Python Modules**

    Install the required Python modules using pip:

    ```bash
    pip install docker
    pip install kubernetes
    ```

## Verification Steps

To verify that the installation has been successful:

1. **Check Python Version**

    Verify that you have the correct version of Python (3.6 or higher) installed:

    ```bash
    python --version
    ```

2. **Check Docker and Kubernetes Installation**

    Verify Docker and Kubernetes are installed correctly:

    ```bash
    docker --version
    kubectl version
    ```

3. **Check Python Modules Installation**

    Check that the Docker and Kubernetes Python modules are installed:

    ```bash
    python -c "import docker; print(docker.__version__)"
    python -c "import kubernetes; print(kubernetes.__version__)"
    ```

    If the commands return the version numbers without any errors, the modules are installed correctly.

## Post-Installation Configuration

After the installation, you need to configure Docker and Kubernetes authentication details in the script.

1. **Docker Authentication**

    Set your Docker username and password in the script:

    ```python
    self.docker_username = "your_docker_username"
    self.docker_password = "your_docker_password"
    ```

2. **Kubernetes Namespace**

    Define the Kubernetes namespace where the deployment will take place:

    ```python
    self.namespace = "your_kubernetes_namespace"
    ```

3. **Docker Registry**

    Specify the Docker registry where the application's Docker image is stored:

    ```python
    self.docker_registry = "your_docker_registry"
    ```

You should now be able to use the DeploymentAutomation script to deploy applications using Docker and Kubernetes.

# Deployment Automation Script Usage Guide

In this guide, we will explain how to use the `DeploymentAutomation` Python class that automates the deployment of applications using Docker and Kubernetes.

## Prerequisites
Ensure Docker and Kubernetes are properly installed in your system. The Python libraries `docker` and `kubernetes` should also be installed.

## 1. Basic Usage

Here is a basic example of using the `DeploymentAutomation` class:

```python
from deployment_automation import DeploymentAutomation

# Initialize the DeploymentAutomation class
deployment = DeploymentAutomation('my_namespace', 'docker_username', 'docker_password', 'docker_registry')

# Deploy an application
deployment.deploy_application('my_app', '/path/to/deployment/config.yml')
```
The `deploy_application` method takes two parameters:
- `app_name` (str): the name of the application to be deployed.
- `deployment_config_path` (str): the path to the Kubernetes deployment configuration file.

## 2. Common Use Cases

### Deploying multiple applications

If you have multiple applications to deploy, you can simply call the `deploy_application` method multiple times:

```python
apps = ['app1', 'app2', 'app3']
for app in apps:
    deployment.deploy_application(app, f'/path/to/{app}/config.yml')
```
In this example, we assume that each application has a separate Kubernetes deployment configuration file located in its respective directory.

## 3. Command-line Arguments

This script does not accept command-line arguments. All parameters are passed directly to the methods of the `DeploymentAutomation` class.

## 4. Expected Output 

Upon successful deployment, the script will log that the application has been successfully deployed. 

Example:
```
2022-01-01 00:00:00,000 - INFO - Successfully deployed application 'my_app'
```
In case of an error during the deployment, an exception will be logged and the script will attempt to rollback the deployment.

Example of an error:
```
2022-01-01 00:00:00,000 - ERROR - Failed to deploy application 'my_app': ApiException()
2022-01-01 00:00:00,000 - INFO - Rolling back deployment of 'my_app'
```

## 5. Advanced Usage

If you want to extend the `DeploymentAutomation` class to add more functionality, you can subclass it. For example, you might want to add a method to scale the deployment:

```python
class ExtendedDeploymentAutomation(DeploymentAutomation):
    def scale_deployment(self, app_name, replicas):
        # your implementation here

# usage
deployment = ExtendedDeploymentAutomation('my_namespace', 'docker_username', 'docker_password', 'docker_registry')
deployment.scale_deployment('my_app', 3)
```
In this example, the `scale_deployment` method would adjust the number of replicas for the given application to the specified number.

# DeploymentAutomation Class API Documentation

## Class Description

The `DeploymentAutomation` class is used to automate the deployment of applications using Docker and Kubernetes. It uses the DockerClient and Kubernetes ApiClient to interact with Docker and Kubernetes respectively. The class also handles authentication with Docker using a username and password and specifies the Docker registry where the application's Docker image is stored. 

## Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| docker_client | DockerClient | A DockerClient object to interact with Docker. |
| k8s_client | ApiClient | A Kubernetes ApiClient object to interact with Kubernetes. |
| namespace | str | The namespace in Kubernetes where the deployment will take place. |
| docker_username | str | The username to authenticate with Docker. |
| docker_password | str | The password to authenticate with Docker. |
| docker_registry | str | The Docker registry where the application's Docker image is stored. |

## Methods

### `deploy_application(app_name: str, deployment_config_path: str) -> None:`

This method deploys the application to Kubernetes.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| app_name | str | The name of the application to be deployed. |
| deployment_config_path | str | The path to the deployment configuration file. |

#### Return Value

This method does not return a value.

## Example

```python
# Import the necessary modules
from docker import DockerClient
from kubernetes import client, config

# Create an instance of the DeploymentAutomation class
deployer = DeploymentAutomation(
    docker_client=DockerClient(base_url='unix://var/run/docker.sock'),
    k8s_client=client.ApiClient(configuration=config.load_kube_config()),
    namespace='default',
    docker_username='my_username',
    docker_password='my_password',
    docker_registry='my_registry'
)

# Deploy the application
deployer.deploy_application('my_app', './my_app_deployment_config.yaml')
```

## Common Patterns and Best Practices

1. **Proper Authentication**: Ensure that the Docker username and password provided are correct to avoid authentication errors during deployment.
2. **Valid Namespace**: Ensure that the specified Kubernetes namespace exists in your cluster.
3. **Docker Image Accessibility**: Ensure that the Docker image for the application to be deployed is available in the specified Docker registry.
4. **Error Handling**: Add appropriate error handling to your deployment script to manage potential issues such as network failures, Kubernetes ApiExceptions, etc.

## ⚙️ Configuration
Configuration options for customizing the application's behavior.

## 🔍 Troubleshooting
Common issues and their solutions.

## 🤝 Contributing
Guidelines for contributing to the project.

## 📄 License
This project is licensed under the MIT License.

## Features

- Complete feature 1: Detailed description
- Complete feature 2: Detailed description
- Complete feature 3: Detailed description

## API Documentation

### Endpoints

#### `GET /api/resource`

Returns a list of resources.

**Parameters:**

- `limit` (optional): Maximum number of resources to return

**Response:**

```json
{
  "resources": [
    {
      "id": 1,
      "name": "Resource 1"
    }
  ]
}
```
