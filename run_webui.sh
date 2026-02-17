#!/usr/bin/env bash

# TODO: Take these from env vars or as parameters.
# TODO: Add ENV=dev to the env vars to enable acces to docs
#  https://docs.openwebui.com/getting-started/advanced-topics/api-endpoints/#swagger-documentation-links
PORT=${PORT:-7772}
NAME=${NAME:-open-webui}
IMAGE=ghcr.io/open-webui/open-webui
VERSION=v0.8.3


if [ ! -S ~/.docker/run/docker.sock ]; then
  echo "The docker service is not running."
  exit 1
fi


if docker ps --format "{{.Names}}" | grep $NAME 2>&1 >/dev/null; then
  echo "There is already a server with name '${NAME}' running."
  echo "Use 'docker stop ${NAME}' to stop it."
  exit 1
fi


if nc -z -v localhost $PORT 2>/dev/null; then
  echo "Port $PORT is already in use."
  exit 1
fi


echo "Starting OpenWebUI container..."
docker run -d \
  -p $PORT:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v $PWD/data:/app/backend/data \
  --rm \
  --name ${NAME} \
  ${IMAGE}:${VERSION}



if [ $? -eq 0 ]; then
  echo "Success"
  echo "Open http://localhost:${PORT} in a browser"
  echo "Use 'docker stop ${NAME}' to stop the OpenWebUI server."
else
  echo "Failed to start the server"
  exit 1
fi
