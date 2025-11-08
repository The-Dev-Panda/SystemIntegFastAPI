from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/create-item/")
async def post_item(item: str):
    return {"item_created": item}