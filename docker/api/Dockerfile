FROM python:3.11

RUN apt update \
  && apt install -y default-mysql-client curl python3-pip \
  && apt install --no-install-recommends -y tzdata \
  && apt clean

# タイムゾーンを日本時間に設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /api

# dockerのapiディレクトリにローカルのpyproject.toml poetry.lockをcopy
COPY pyproject.toml poetry.lock ./

# ローカルのappディレクトリをdockerのapi内にcopy
COPY app ./app

# 環境変数を設定
ENV PYTHONPATH=/api

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
