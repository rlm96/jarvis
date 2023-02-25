docker build -t jarvis-watchman .
docker run -p 6667:6667/udp --name jarvis-watchman -d jarvis-watchman