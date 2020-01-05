FROM python:3.6-alpine

WORKDIR /app
COPY . /app

RUN apk upgrade -U \
&& apk add --no-cache ca-certificates build-base libffi-dev ffmpeg opus-dev
RUN pip install --upgrade pip pipenv
RUN pipenv install
CMD ["pipenv", "run", "python", "main.py"]