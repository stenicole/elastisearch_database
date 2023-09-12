FROM ubuntu:latest
RUN apt-get update && apt-get install python3-pip -y &&  apt-get install curl && sudo apt-get install elasticsearch
RUN apt-get clean \ && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp*
WORKDIR /peupl_BDD/data/
ADD elastic.sh /peupl_BDD/elastic.sh
ADD peupl_BDD.py /peupl_BDD/peupl_BDD.py
ADD DataElectProdData1.csv /peupl_BDD/DataElectProdData1.csv
WORKDIR /peupl_BDD/
ENTRYPOINT python3 peupl_BDD.py
