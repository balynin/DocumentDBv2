FROM python:3.10

RUN mkdir /app

WORKDIR /app

COPY . .

RUN apt update \
  && apt -y install tesseract-ocr \
  && apt -y install tesseract-ocr-rus


RUN pip install -r requirements.txt

