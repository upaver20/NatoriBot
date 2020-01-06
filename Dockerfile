FROM python:3.6-alpine

WORKDIR /app
COPY . /app
RUN apk upgrade -U \
&& apk add --no-cache ca-certificates gcc linux-headers musl-dev make libffi-dev ffmpeg opus-dev \
&& pip install pipenv --no-cache-dir \
&& pipenv install --system --deploy \
&& pip uninstall -y pipenv virtualenv-clone virtualenv \
&& apk del make linux-headers musl-dev libffi-dev --purge \
&& rm -rf ~/.cache/
CMD ["python", "main.py"]
