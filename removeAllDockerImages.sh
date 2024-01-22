#!/bin/bash

# Prune all stopped containers
docker container prune -f

# Remove all Docker images
docker rmi $(docker images -q)
