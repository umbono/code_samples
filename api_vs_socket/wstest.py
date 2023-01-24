import asyncio
import pytest
import websockets
from fastapi import WebSocket
from samplews import app

@pytest.mark.asyncio
async def test_websocket_endpoint():
    uri = "ws://localhost:5001/ws"  # change this to the correct URI of your endpoint
    async with websockets.connect(uri) as websocket:
        # Send a message to the endpoint
        await websocket.send("Hello")
        # Receive a message from the endpoint
        data = await websocket.recv()
        # Assert that the message received is as expected
        assert data == "Message text was: Hello"



