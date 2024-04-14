#!/bin/bash

# Potegni sliko iz DockerHub
docker pull kalkulator:latest

# Poženi vsebnik z imenom "moj_vsebnik"
docker run --name MauserWas -d -p 8080:80 kalkulator:latest

