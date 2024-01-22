docker container prune -f
docker rmi $(docker images -q)
