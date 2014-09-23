FROM ubuntu
MAINTAINER jmiller@adops.com

RUN sudo apt-get update

RUN apt-get install -y git python

ADD /hellolib /hellolib

WORKDIR /hellolib
