# NatoriBot

さなボタン(2)様にある音声をDiscordに流すBot

## Setup

1. ```.env``` ファイルを作成/編集

```cp sample_env .env```

2. data ディレクトリ内に posts.json を用意

### そのまま動かす場合

```pip install pipenv```

```pipenv install```

```pipenv run python main.py```

### Dockerで動かす場合

```docker build -t hoge:fuga```

```docker run --name piyo --env_file .env -v $(pwd)/data:/app/data hoge:fuga```

## Usage

### join

```@your_bot_name join```

ボイスチャンネルにいる際，```.env``` ファイルで指定したテキストチャンネルでBotに対してメンションで```join```

### talk

```おは```

```.env``` ファイルで指定したテキストチャンネルで，部分一致で音声の再生

### leave

```@your_bot_name leave```

```.env``` ファイルで指定したテキストチャンネルでBotに対してメンションで```leave```
