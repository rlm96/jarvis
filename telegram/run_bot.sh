docker build -t jarvis-telegram .
docker run --restart always --name jarvis-telegram -d jarvis-telegram