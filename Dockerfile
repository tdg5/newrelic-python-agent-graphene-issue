FROM python:3.10.4-bullseye

COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY src /app

ENV PYTHONPATH=/app

ENTRYPOINT ["uwsgi"]

CMD ["--yaml", "/app/uwsgi.yaml"]
