#/bin/bash run.sh > bootstrap.sh

# this updates and installs lxc-docker
curl -sSL https://get.docker.io/ubuntu/ | sudo sh
usermod -g docker vagrant

# install pip for acceptance test
sudo apt-get install -y python python-pip
