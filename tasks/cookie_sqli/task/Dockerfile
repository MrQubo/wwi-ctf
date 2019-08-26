FROM php:7.3-apache-buster

RUN apt-get update -y && \
    apt-get install -y libpq-dev && \
    docker-php-ext-install pgsql

COPY ./src/ /var/www/html/
