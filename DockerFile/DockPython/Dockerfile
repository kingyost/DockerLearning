FROM ubuntu:16.04 
MAINTAINER Eric Yost 
ENV NAME Eric
RUN apt-get update && \
apt-get install -y python 
COPY hello.py .
ENTRYPOINT ["python", "hello.py"]