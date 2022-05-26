FROM python:3.10.4-bullseye

COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./hypercorn_conf.py /tmp/hypercorn_conf.py

COPY src /app

ENV PYTHONPATH=/app

ENTRYPOINT ["hypercorn"]

CMD ["--config", "file:/tmp/hypercorn_conf.py", "entry:app"]
