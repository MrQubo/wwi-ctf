FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip firefox firefox-geckodriver

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY bot.py .

ENTRYPOINT ["python3", "bot.py"]
