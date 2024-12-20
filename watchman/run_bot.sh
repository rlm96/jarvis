docker build -t jarvis-watchman -f Dockerfile ..
docker run --network host --restart always --name jarvis-watchman -d jarvis-watchman