from fastapi import FastAPI
from typing import Dict, Any
import uvicorn
import uuid

app = FastAPI()

@app.get("/")
async def sample():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Dict[str, Any]):
    # Code to handle the creation of an item goes here
    item_id = str(uuid.uuid4())
    return {"name": item["name"], "id": item_id}

if __name__ == '__main__':
    uvicorn.run("sampleapi:app", host="0.0.0.0", port=5000, reload=True, workers=2)
