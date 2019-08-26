FROM php:7.3.8-fpm-buster

RUN apt-get update -y && \
    apt-get install -y libpq-dev && \
    docker-php-ext-install pgsql

WORKDIR /opt/app/
RUN useradd --user-group --no-create-home --uid 1001 --shell /bin/bash app

ENTRYPOINT ["/opt/entrypoint.sh"]
COPY ./entrypoint.sh /opt/entrypoint.sh

COPY ./src/ /opt/app/

RUN chown root:root -R /opt/ && \
    chmod u+x /opt/entrypoint.sh && \
    chown 1001:1001 -R /opt/app/
