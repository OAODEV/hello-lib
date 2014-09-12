from ubuntu
maintainer jmiller@adops.com

run sudo apt-get update

run apt-get install -y python python-pip
run pip install -U pip

run mkdir /docks
run echo '<h1>stub docs</h1>' > docks/index.html

workdir /docks
cmd python -m SimpleHTTPServer