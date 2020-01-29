FROM ubuntu
MAINTAINER CHRIS<christophe.desterke@inserm.fr>
RUN apt-get update -y
RUN apt-get install -y git

FROM python:3.7
RUN pip install --upgrade pip && \
    pip install numpy==1.17.4 Keras==2.3.1 tensorflow==2.0.0 scikit-learn==0.22 


WORKDIR /home
RUN git clone https://github.com/cdesterke/eightbio.git
WORKDIR /home/eightbio

