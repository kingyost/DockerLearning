FROM ubuntu:16.04 
MAINTAINER Kingyost
RUN apt-get update && \
apt-get install -y python3 && \
apt-get pip install Flask
COPY helloFrame.py .
ENTRYPOINT ["python3", "helloFrame.py"]
