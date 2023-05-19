FROM python:3

ENV PYTHONBUFFERED 1

WORKDIR /docker_app

ADD . /docker_app

COPY ./requirements.txt /docker_app/requirements.txt

RUN pip install -r requirements.txt

COPY . /docker_app

ENV DJANGO_SETTINGS_MODULE=core.settings


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]