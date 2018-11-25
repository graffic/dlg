#!/usr/bin/env bash

echo "1. Build image"
IMAGE="docker.io/graffic/dlg"

docker build -t $IMAGE .
docker push $IMAGE

echo "2. Deploy to cloud foundry"
cf push DLGAssignment --docker-image $IMAGE -i 1 -m 256M