FROM python:3.6

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
      libopus-dev \
      libsodium-dev \
      wget \
      xz-utils
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
      && tar Jxvf ./ffmpeg-release-amd64-static.tar.xz \
      && cp ./ffmpeg*amd64-static/ffmpeg /usr/local/bin/
RUN pip install --upgrade pip
RUN pip install --upgrade pipenv
RUN pipenv install
CMD ["pipenv", "run", "python", "main.py"]