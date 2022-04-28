# Encryptor
[![.github/workflows/build.yml](https://github.com/slo-fi/encryptor/actions/workflows/build.yml/badge.svg)](https://github.com/slo-fi/encryptor/actions/workflows/build.yml)  
Encryptor is an example terminal app that can generate and decrypt ciphers that even supports importing and exporting to files. It's meant to convey my style of Python programming.

# Installation Guide
Two methods of installation are provided. Do note that these assume a Linux/UNIX system, though they should work on Windows provided you use PowerShell.
## Use the Docker Image (recommended for platform independence)
The Docker image is the preferred method of installation. It has the most up-to-date changes and is less likely to break as well as easier to update compared to building it directly from source.
### Prequisites
All you need to install is:
- [Docker](https://www.docker.com/products/docker-desktop/)
### Downloading
Firstly, if you don't already have one, you'll have to create a [Docker Hub](https://hub.docker.com/signup) account.  
Next, pull the latest image directly from the encryptor repository on Docker Hub.
```bash
docker pull shaurcode/encryptor:latest
```
And you're done! To start up a fresh container running encryptor, simply run:
```bash
docker run -it shaurcode/encryptor
```
## Build From Source Using Pipenv
This is advised when Docker is either not available for your system or not desired. Building from source will provide the platform-specific executable for your system.
### Prerequisites
This requires the following be installed:
- [Python 3.9](https://www.python.org/downloads/release/python-3912/) - Obviously!
- [Pipenv](https://pipenv.pypa.io/en/latest/) - Handles packages and will build the executable for you
- [git](https://git-scm.com/downloads) - You'll need this to clone the repository
### Building
First, clone the repository to your current directory using git. 
```bash
git clone https://github.com/slo-fi/encryptor.git
```
Then change into the `encryptor` directory.
```bash
cd encryptor
```
You'll need to install the packages using ```pipenv```. However, this will create a virutal environment in the process. To avoid potentially polluting your system with them, it is advised to create the environment directly in this folder.
```bash
PIPENV_VENV_IN_PROJECT=1 pipenv install
```
Afterwards, simply run:
```bash
pipenv run build
```
And you should find the final executable in a newly created ```dist/``` directory. Feel free to move this file anywhere and get rid of the cloned directory, as the executable contains all the dependencies needed to run encryptor.

