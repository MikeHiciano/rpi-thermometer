#!/bin/bash

sudo apt-get update
sudo apt-get install -y git-core
sudo apt-get install -y build-essential python3-dev python3-pip
pip3 install -r requirements.txt
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install 
echo "************ INSTALATION COMPLETE ***************"