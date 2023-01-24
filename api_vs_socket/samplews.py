from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
        
if __name__ == '__main__':
    uvicorn.run("samplews:app", host="0.0.0.0", port=5001, reload=True, workers=2)