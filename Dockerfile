# syntax=docker/dockerfile:1

FROM python:latest
WORKDIR /
COPY . /
EXPOSE 8000
CMD ["python", "test.py"]