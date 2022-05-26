from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_full_stack():
    return {"message": "Hello, Full Stack!"}
