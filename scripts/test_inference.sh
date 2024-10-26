#!/bin/bash

# Test data (replace with data your API expects)
TEST_DATA='{"input_data": "[0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.09,1.0,296.0,15.3,396.9,4.98]"}'

# Send a POST request to the /predict endpoint
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d "$TEST_DATA"

# docker run -d -p 8080:80 --name my_local_container $IMAGE_NAME:latest