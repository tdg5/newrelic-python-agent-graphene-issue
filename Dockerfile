FROM python:3.10.4-bullseye

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./test_proj /app/test_proj
COPY ./newrelic.ini /app/newrelic.ini


ENTRYPOINT ["python"]

CMD ["-m", "test_proj.entry"]
