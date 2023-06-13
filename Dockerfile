FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y gcc time

COPY ./requirements.txt /app/

RUN python -m venv venv && pip install -r requirements.txt

COPY . /app

ENV NEW_RELIC_LICENSE_KEY="$NEW_RELIC_LICENSE_KEY"

CMD bash /app/benchmark.sh
