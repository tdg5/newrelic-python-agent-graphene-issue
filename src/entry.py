from flask import Flask
import asyncio

RESPONSE_HTML = "<p>Hello, Full Stack!</p>"

app = Flask("Hello Full Stack")


@app.route("/")
def hello_full_stack():
    return RESPONSE_HTML


@app.route("/async")
async def hello_full_stack_async():
    await asyncio.sleep(1)
    return RESPONSE_HTML
