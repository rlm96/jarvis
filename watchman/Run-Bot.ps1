docker build -t jarvis-watchman -f Dockerfile ..
docker run --network host --name jarvis-watchman -d jarvis-watchman