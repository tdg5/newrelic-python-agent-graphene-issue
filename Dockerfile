FROM python:3.10.4-bullseye

COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./hypercorn_conf.py /tmp/hypercorn_conf.py

COPY src /app

# Example secret file
COPY ./VERSION /app/secrets/hello_full_stack_version

# Example config file
COPY ./config/config.example.yaml /tmp/config.yaml

ENV PYTHONPATH=/app

ENV \
  HELLO_FULL_STACK_NAME='hello-full-stack' \
  HELLO_FULL_STACK_SECRETS_DIR_PATH='/app/secrets' \
  HELLO_FULL_STACK_YAML_CONFIG_PATH='/tmp/config.yaml'

ENTRYPOINT ["hypercorn"]

CMD ["--config", "file:/tmp/hypercorn_conf.py", "hello_full_stack.entry:api"]
