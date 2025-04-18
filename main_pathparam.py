# Important infos:
# [1] openAPI schema : http://127.0.0.1:8000/openapi.json
from fastapi import FastAPI

app = FastAPI()


@app.get("/item/{item_id}")
# async def root(): # used with library requires `await`
async def read_item(item_id: int):
    return {"item_id": item_id}