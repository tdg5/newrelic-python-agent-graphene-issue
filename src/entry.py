"""
Example/template implementation of an API microservice.
"""


from fastapi import FastAPI


app = FastAPI(
    description=__doc__,
    title="hello-full-stack",
)


@app.get("/")
async def hello_full_stack():
    """Minimal example GET endpoint."""
    return {"message": "Hello, Full Stack!"}
