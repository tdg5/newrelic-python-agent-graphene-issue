FROM python:3.10.4-bullseye

ARG AWS_CODEARTIFACT_AUTH_TOKEN
ARG HELLO_FULL_STACK_GIT_SHA
ARG HELLO_FULL_STACK_VERSION

WORKDIR /app

# Configure pip so we can access packages via AWS CodeArtifact
RUN pip config set global.index-url "https://aws:${AWS_CODEARTIFACT_AUTH_TOKEN}@neural-magic-private-498127099666.d.codeartifact.us-east-1.amazonaws.com/pypi/nm-py/simple/"

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./hypercorn_conf.py /tmp/hypercorn_conf.py

COPY ./src /app

ENV PYTHONPATH=/app

ENV HELLO_FULL_STACK_GIT_SHA=${HELLO_FULL_STACK_GIT_SHA}
ENV HELLO_FULL_STACK_NAME='hello-full-stack'
ENV HELLO_FULL_STACK_VERSION=${HELLO_FULL_STACK_VERSION}

ENTRYPOINT ["hypercorn"]

CMD ["--config", "file:/tmp/hypercorn_conf.py", "hello_full_stack.entry:api"]
