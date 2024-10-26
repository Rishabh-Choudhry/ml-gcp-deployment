
#!/bin/bash

# Image name (should match the name used in the build script)
IMAGE_NAME="xgboost-model"

# Run the Docker container
# sudo docker run -d -p 5000:5000 $IMAGE_NAME:latest
sudo docker run -it --rm -p 5000:5000 $IMAGE_NAME:latest /bin/bash