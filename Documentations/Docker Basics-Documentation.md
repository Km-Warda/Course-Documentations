# Containers
Containers are packages of software that contain all of the necessary elements to run in any environment, virtualizing the operating system and run anywhere, from a private data center to the public cloud or even on a developer's personal laptop.

##### - Before containers, installation process was different for each OS environment, besides the chance of occurrence of n error.

##### - After containers, installation has its own isolated environment & packaged with all configuration needed. Installation of the container app is done with only a docker command fetching & installing the app. And this enabled the installation of different versions of the same app without any conflicts.

Containers technically is layers of images, the base is mostly **Linux Base Image** because its small size, and the application image on top. Layers being downloaded in the picture.
![Containers Layers](https://user-images.githubusercontent.com/109697567/205089846-80099196-adcd-4a71-8dc8-9c8c6bea8222.png)

*note:* Docker image is the **non running package** while Docker container is what is **running service** is called.


# Main Docker Commands
* #### docker pull redis
*to pull from docker hub, here last version of redis is pulled.
* #### docker run redis:4.0.14
*to start the image, if not found locally, will be pulled from the hub & starts it, here v4.0.14 of redis is pulled.
* #### docker run -d redis
*starts a container in detach mode, in the background with no result on the screen.
* #### docker stop 8381867e8242
*stops the container with container ID 8381867e8242.
* #### docker start 8381867e8242
*restarts the container with container ID 8381867e8242.
* #### docker ps
*lists running containers
* #### docker ps -a
*lists all containers, running or stopped.
* #### docker images
*list all local images.
* #### docker run -p6000:6379
*starts container of port no.6379 and binds it to host port no.6000, in order to start using it.

*note:* You can't use same host port for the same container port.
* #### docker run -d -p6001:6379 --name contanier_name redis:4.0
*naming a container instead of dealing with IDs.
* #### docker logs container_name
* #### docker logs 8381867e8242
*show logs produced by this container.
* #### docker exec -it 8381867e8242 /bin/bash
*open interactive terminal for the container to deal with it, edit configuration files, etc. exit with "exit" command. -it option stands for interactive terminal.

# Docker Network
Docker creates its own isolated networks where the containers are running in, any containers inside will communicate with only the container name as they are in the same network. And the applications that runs outside the network willl communicate using localhost:*(PORT_NO.)*
By default Docker already generates some networks on its own.
![Docker Networks](https://user-images.githubusercontent.com/109697567/205089912-5e612c43-b5c8-4252-92a2-f83603de5a05.png)

* #### docker network ls
*list docker networks
* #### docker network create Network1
*create docker network

*note:* Check the image page in the docker hub to check all available configurations.
For example take notice of the following run command 
![Options Run Command](https://user-images.githubusercontent.com/109697567/205089948-3c6a486c-4d66-4559-a8ef-c57c1b831600.png)
# Docker Compose
Instead of applying the last command for configuring multiple containers, Docker compose tool lets you put all the configuration in a structured way in one file.
![Docker Compose](https://user-images.githubusercontent.com/109697567/205089981-d8176d74-55e6-4922-929c-0d69fc2ba0fe.png)

* #### docker-compose -f config.yaml up
*Starts the containers in config.yamel file using the docker compose tool.*
* #### docker-compose -f config.yaml down
*Shuts down the containers in config.yamel file using the docker compose tool.*

*note:* Docker Compose automatically creates Networks for the container & takes care of connection. And it removes it as well with the *down* command.

# Docker Volumes
Assume a container runs on a host & it has a virtual file system where the data is stored. If the container is removed or restarted it will start in a fresh state & the data is lost.

The way Docker volumes work is that it mounts the physical host file system path into the virtual file system, so whenever the container writes on its file system it automatically updates the host file system, & vice versa.

### There are 3 types of volumes:
- ### **Host Volumes**
#### docker run -v /home/physyicalFS:/var/virtualFS
*you decide where the host file system is
- ### *Anonymous Volumes*
#### docker run -v /var/virtualFS
*no host file reference & is created automatically by Docker.
- ### *Named Volumes*
#### docker run -v PathName:/var/virtualFS
*like the anonymous volumes but you reference the volumes by name*

*note:* The Named Volumes is the one that should be used in production because there is additional benefits to letting Docker manage the volume directories on the host.
![Docker Volumes](https://user-images.githubusercontent.com/109697567/205090057-0e4bd7a6-dbfd-4fb5-8662-9c820c5313bb.png)
*note:* For applying volumes using Docker-compose, use the "volumes:" attribute and enter the same data of the desired volume type as before. Then enter the desired volume to be mounted at the end also using the "volumes:" attribute.

This means you can mount multiple containers to the same volume of they needed to share the data.
![Volumes in Docker-Compose](https://user-images.githubusercontent.com/109697567/205090094-72b7e735-3a5b-433e-88e7-8be4b23ce5a0.png)

### Docker volume locations :
![Docker Volume Locations](https://user-images.githubusercontent.com/109697567/205090132-519692cf-474f-4fb0-8d98-1cf47a8f534a.png)
*note:* On MAC OS specifically, Docker creates a Linux VM and stores all Docker data there. so if you executed *ls /var/lib/docker*, a "no such file or directory" message will appear. You can access the file through accessing the VM terminal by "screen" command. & the data will be present there. To exit the screen press `ctrl+A+K` {For MAC OS}.

# Building Your Own Docker Image
You can build a docker image from a docker file, docker files must be names `Dockerfile` & you will see it has the docker icon on a code executer.

Docker files have a specific syntax, here we have:
- `FROM` for setting the image desired to be used.
- `ENV` for setting environmental variables.
- `RUN` for running Linux commands on the container not locally.
- `COPY` for copying locally.
- `CMD` for entry point commands.
![[Pasted image 20230210183952.png]]
*Note:* Whenever you adjust a Docker file you have to rebuild its Docker image.

Now we can use the command `build` :
`docker build -t app-name:v.1 .`
In the command before we set a name for the docker image "app-name", & a tag for it "v.1", and we gave the location of the docker file to be used for this docker image to be created, in this case we used a "." because it is in the same directory, but if the docker file is somewhere else the path is given instead.

# Deleting a docker image
For deleting a Docker image you have to delete the container first `docker rm`
then remove the docker image `docker rmi`

# Docker Repositories
There are Public Docker repositories like "Docker Hub" where everyone can download images there, & there are private repositories, basically for companies private docker images.
*ex:* Gitlab container repository
- In order to push/pull an image to a private docker repository you must have the credentials required.
- The repository location is included in the image name
![Pasted image 20230214193709](https://user-images.githubusercontent.com/109697567/220483930-b36d2ba4-1039-4836-b185-19d541f7f09c.png)
