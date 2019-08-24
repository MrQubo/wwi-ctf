FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    python \
    python-pip \
    python3 \
    python3-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip setuptools wheel virtualenv virtualenvwrapper
RUN pip3 install -U pip setuptools wheel ruamel.yaml

RUN mkdir -p /tests/artifacts/.virtualenvs/
ENV WORKON_HOME=/tests/artifacts/.virtualenvs/

ENTRYPOINT ["/tests/entrypoint.sh"]
COPY ./entrypoint.sh /tests/entrypoint.sh
COPY ./run_test.py /tests/run_test.py
