import asyncio
import websockets
import time
from helpers import load_config

async def send_periodic_messages():
    host, port = load_config('client')
    uri = f'ws://{host}:{port}'
    async with websockets.connect(uri) as websocket:
        while True:
            timestamp = str(int(time.time()))
            await websocket.send(timestamp)
            print(f"Sent: {timestamp}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(send_periodic_messages())
