from setuptools import setup, find_packages

setup(
    name='DeploymentAutomation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'docker==5.0.0',
        'kubernetes==18.20.0',
        'PyYAML==5.4.1',
    ],
)