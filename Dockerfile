FROM python:3.6-alpine

WORKDIR /app
COPY . /app
RUN apk upgrade -U \
&& apk add --no-cache ca-certificates build-base libffi-dev ffmpeg opus-dev \
&& pip install pipenv --no-cache-dir \
&& pipenv install --system --deploy \
&& pip uninstall -y pipenv virtualenv-clone virtualenv \
&& rm -rf ~/.cache/pip
CMD ["python", "main.py"]
