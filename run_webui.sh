#!/usr/bin/env bash

# TODO: Take these from env vars or as parameters.
# TODO: Add ENV=dev to the env vars to enable acces to docs
#  https://docs.openwebui.com/getting-started/advanced-topics/api-endpoints/#swagger-documentation-links
PORT=7772
NAME=open-webui
IMAGE=ghcr.io/open-webui/open-webui
VERSION=v0.5.20


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
# XXX: I'm changing `main` to a pinned version.  With `main`
# it isn't picking up the latest version, like I expected.
# I'm getting notifications of a new version available.
# Since I'm getting the notifications, because the setting
# "Toast notifications for new updates" is enabled, I will
# use that to know when I need to come here and update the
# pinned version.

docker run -d \
  -p $PORT:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
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
