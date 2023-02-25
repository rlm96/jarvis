docker build -t jarvis-watchman .
docker run --network host --name jarvis-watchman -d jarvis-watchman