FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app

ENV PORT=8000

RUN python manage.py collectstatic --noinput

CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT
