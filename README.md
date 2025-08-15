# ECHO

## Sandbox Web Application for SSTI

***ECHO*** is a **deliberately vulnerable Flask web application** designed as a sandbox environment for learning **Server-Side Template Injection (SSTI)**.

**This application is an educational tool and should never be deployed in a production environment.**

---

## Setup

You can run ***ECHO*** either using a docker or simply with a Python command. However, it is **recommended** to use dockers since running the application directly on your system could compromise it.  

### 1. Clone the Repository

```bash
git clone ----
cd app
```

### 2. Build the Docker Image

If you don't have `docker` installed, you need to install it first to run the container.  

Follow [Docker installation procedure](https://docs.docker.com/engine/install/) for installing `docker` based on your platform.

```bash
docker build -t echo .
```

- `docker build` : `docker` command to build a Docker image  
- `-t echo` : Optional flag for naming a Docker container
- `.` : Directory in which `Dockerfile` is in (Current directory)

### 3. Run the Docker Container

```bash
docker run -p 8000:8000 echo
```

- `docker run` : `docker` command to run a Docker container
- `-p 8000:8000` : Mapping of host port and container port (host:container)
- `echo` : Name of the Docker container you are running

---

## Accessing ***ECHO***

After running the Docker container, you can simply browse [http://127.0.0.1:8000/](http://127.0.0.1:8000/). If you specified a different port when you ran the Docker container, use that port number instead of 8000.

---

## Stopping the Container

Container ID or name is required to stop a Docker image.

```bash
docker ps
```

- `docker ps` - `docker` command for listing containers

```bash
docker stop <container_id_or_name>
```

- `docker stop` : `docker` command for stopping containers
- `container_id_or_name` : Container ID or name we get from running the previous command

## **Disclaimer**

***ECHO*** is designed **intentionally to be vulnerable** to Server-Side Template Injection (SSTI) attacks for educational purposes. Please refrain from running the application in production environments.

---
