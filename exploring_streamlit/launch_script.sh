#!/bin/bash

######################################################################################
# Build the Docker image
######################################################################################
docker build -t streamlit_example:1.0 .

# If using containerd as container engine, can use nerdctl
# nerdctl build -t streamlit_example:1.0 .

######################################################################################
# Run docker container
######################################################################################
docker run -d --name example-1 -p 8501:8501 streamlit_example:1.0

######################################################################################
# Push the DOcker image to container registry (Optional step)
# Only if one wants to push it to their container registry
# Uncomment below, if intended to use.
######################################################################################
# docker tag streamlit_example:1.0 my_docker_user_name/streamlit_example:1.0
# docker push my_docker_user_name/streamlit_example:1.0

######################################################################################
# Start application using Docker Compose (if require multi container approach)
######################################################################################
# docker-compose up