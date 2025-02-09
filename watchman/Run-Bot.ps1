docker build -t jarvis-watchman -f Dockerfile ..
# --network host does not work on Windows due to Docker limitations
# https://github.com/docker/for-mac/issues/2716
# https://docs.docker.com/engine/network/drivers/host/#docker-desktop
# https://docs.docker.com/engine/network/drivers/host/#limitations
docker run --network host --name jarvis-watchman -d jarvis-watchman