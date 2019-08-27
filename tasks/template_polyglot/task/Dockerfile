FROM python:3.7.4-buster

RUN apt-get update -y

WORKDIR /opt/app/
RUN useradd --user-group --no-create-home --uid 1001 --shell /bin/bash app && \
    mkdir -p /opt/app/files/ /opt/app/uploads/

COPY ./requirements.txt /opt/requirements.txt
RUN pip install --upgrade -r /opt/requirements.txt && rm /opt/requirements.txt

ENTRYPOINT ["/opt/entrypoint.sh"]
COPY ./entrypoint.sh /opt/entrypoint.sh

COPY ./app/ /opt/app/
RUN chown root:root -R /opt/ && \
    chown root:1001 -R /opt/app/ && \
    chmod u+x /opt/entrypoint.sh && \
    chmod g+w /opt/app/files/ && \
    chmod g+w /opt/app/uploads/
