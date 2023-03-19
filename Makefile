debian:
	apt install -y python3 python3-pip
	pip3 install -r requirements.txt --user

fedora:
	dnf install -y python3 python3-pip
	pip3 install -r requirements.txt --user 

install:
	pip3 install -r requirements.txt --user

run:
	python3 app.py