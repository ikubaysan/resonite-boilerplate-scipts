import asyncio
import websockets
import time

async def send_periodic_message():
    async with websockets.connect('ws://10.0.0.106:8765') as websocket:
        while True:
            current_time = str(int(time.time()))
            await websocket.send(current_time)
            print(f"Sent message '{current_time}' to server")
            await asyncio.sleep(1)  # Send message every 1 second

asyncio.get_event_loop().run_until_complete(send_periodic_message())
