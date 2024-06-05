FROM python:3.11

RUN apt update \
  && apt install -y default-mysql-client curl python3-pip \
  && apt install --no-install-recommends -y tzdata \
  && apt clean

WORKDIR /app/

# タイムゾーンを日本時間に設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Poetryのインストール 
RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /app/

COPY . /app

# 依存関係のみをインストール
RUN poetry install --no-root --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
