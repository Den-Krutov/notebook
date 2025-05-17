FROM python:3.13.2

RUN mkdir -p usr/src/app/
WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ../../app/requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .
