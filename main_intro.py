# Important infos:
# [1] openAPI schema : http://127.0.0.1:8000/openapi.json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
# async def root(): # used with library requires `await`
def root():
    return {"message": "Hello World"}