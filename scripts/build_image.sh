#!/bin/bash

# Image name (choose any name you like)
IMAGE_NAME="xgboost-model"

# Build the Docker image
docker build -t $IMAGE_NAME:latest .


# chmod +x run_container.sh

