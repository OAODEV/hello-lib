FROM ubuntu
MAINTAINER jmiller@adops.com

RUN sudo apt-get update

RUN apt-get install -y git python

ADD . /hellolib

WORKDIR /hellolib

# expose the git port
EXPOSE 9418

# run the git service. This will export the repository on the git port allowing
# downstream projects to access this library.
CMD git daemon --verbose \
               --export-all \
               --base-path=.git \
               --reuseaddr \
               --strict-paths \
                   .git/
