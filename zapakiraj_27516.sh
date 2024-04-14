#!/bin/bash

# Naredi Docker sliko
docker build -t kalkulator:latest .

# Prijava v DockerHub
echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin

# Potisni sliko na DockerHub
docker push kalkulator:latest

