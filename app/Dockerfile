# syntax=docker/dockerfile:1.4

FROM python:3 AS builder
EXPOSE 8000

WORKDIR /usr/src/app

COPY requisitos.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requisitos.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8005"]
