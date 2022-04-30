# Encryptor
[![.github/workflows/build.yml](https://github.com/slo-fi/encryptor/actions/workflows/build.yml/badge.svg)](https://github.com/slo-fi/encryptor/actions/workflows/build.yml)  
Encryptor is an example terminal app that can generate and decrypt ciphers that even supports importing and exporting to files. It's meant to convey my style of Python programming.

# Installation Guide
Two methods of installation are provided. Do note that these assume a Linux/UNIX system, though they should work on Windows provided you use PowerShell.
## Build From Source Using Pipenv (Recommended)
This is the preferred method of installation. This will create a platform-dependent executable for your system that is completely self-contained and can run on its own. 
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
mkdir .venv && pipenv install
```
Afterwards, simply run:
```bash
pipenv run build
```
And you should find the final executable in a newly created ```dist/``` directory. Feel free to move this file anywhere and get rid of the cloned directory, as the executable contains all the dependencies needed to run encryptor.
### Handling Errors
If an error occurs during installation, it'll likely be because some platform-dependent libraries are not installed. Check the output for details on what is missing and install them using your system's package manager.
## Use the Docker Image
The Docker Universal distribution of Encryptor can only work with local files provided you mount them to the container using a [Docker Bind Mount](https://docs.docker.com/storage/bind-mounts/) or [Docker Volume](https://docs.docker.com/storage/volumes/). The advantage of this installation method is that the Docker Hub Image is always up-to-date with the latest changes to the repo and it's always easier to ```docker pull``` to update your image as opposed to building the entire thing from source again.
### Prequisites
All you need to install is:
- [Docker](https://www.docker.com/products/docker-desktop/)
### Downloading
Firstly, if you don't already have one, you'll have to create a [Docker Hub](https://hub.docker.com/signup) account.  
Next, pull the latest image directly from the encryptor repository on Docker Hub.
```bash
docker pull shaurcode/encryptor:latest
```
And you're done! To start up a fresh container running encryptor (without mounts), simply run:
```bash
docker run -it shaurcode/encryptor
```
To bind mount files contained in ```/example``` to ```/files``` on a new container, use:
```bash
docker run -it --mount type=bind,source=/example,target=/files shaurcode/encryptor
```
