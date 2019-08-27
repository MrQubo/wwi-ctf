FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN python3 ./manage.py migrate
RUN python3 ./manage.py setup

ENTRYPOINT ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
