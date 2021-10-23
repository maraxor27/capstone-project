FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /myapp