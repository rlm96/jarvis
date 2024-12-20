docker build -t jarvis-telegram -f Dockerfile ..
docker run --restart always --name jarvis-telegram -d jarvis-telegram