FROM python:3.15.0b2-trixie

WORKDIR /app

COPY . /app

RUN pip install django

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]