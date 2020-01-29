# EIGHTBIO
## Eightbio is a deeplearning model used to predict NinetyGL events
----------
#### This predictive artificial intelligence model is based on a system architecture which depends on several python language libraries and whose version compatibility must be respected to be executed. It is for these reasons that the Docker type container system was chosen to deploy this mathematical model. Indeed, this model uses the python language version 3.7.3 with interdependent of distinct libraries. For the good functionality of the program, these libraries must be installed with specific versions to be compatible, such as: tensorflow version 2.0.0, scikit-learn version 0.21.2, keras version 2.3.1 and numpy version 1.16.4. The Docker container will be able to build a system encompassing all these dependencies of mathematical libraries.
----------
![os](https://github.com/cdesterke/eightbio/blob/master/os.jpg)
----------
### STEP 1: install DOCKER software one your operating system
#### on MAC visit: https://docs.docker.com/docker-for-mac/
#### on WINDOWS visit: https://docs.docker.com/docker-for-windows/
#### on LINUX: command lines depending of your distribution

----------
### STEP 2: clone the eightbio repository
![clone](https://github.com/cdesterke/eightbio/blob/master/clone.jpg)

----------
### STEP 3: Build the docker with the command line in the eightbio clone directory

# docker build - < Dockerfile -t eightbio:0.1.1
#### example under ubuntu docker organize the eightbio:0.1.1
![build](https://github.com/cdesterke/eightbio/blob/master/small.jpg)

----------
### STEP 4: verified the presence of the image "eightbio:0.1.1" when the job is complete 
# docker image ls
![image](https://github.com/cdesterke/eightbio/blob/master/image.jpg)
## the container image "eightbio:0.1.1" has a size of 1.68 GB

----------
### STEP 5: RUN the image "eightbio:0.1.1" 
# docker run -it eightbio:0.1.1 /bin/bash
![run](https://github.com/cdesterke/eightbio/blob/master/run.jpg)
## Prompt is inside the docker
----------
### STEP 6: RUN the predictive software "eightbiointeractive.py" inside the docker
# python3 eightbiointeractive.py

