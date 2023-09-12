FROM ubuntu:latest
MAINTAINER Steve
RUN apt-get update && apt-get install python3-pip -y && pip3 install flask==1.1.1 && pip3 install requests 
RUN apt-get clean \ && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp*
WORKDIR /authent/data/
ADD authentication.py /authent/authentication.py
WORKDIR /authent/
ENTRYPOINT python3 authentication.py
