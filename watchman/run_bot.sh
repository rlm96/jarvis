docker build -t jarvis-watchman .
docker run --network host --restart always --name jarvis-watchman -d jarvis-watchman