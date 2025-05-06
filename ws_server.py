import asyncio
import websockets
from helpers import load_config

connected_clients = set()

async def chat_server(websocket):
    client_ip, client_port = websocket.remote_address
    client_id = f"{client_ip}:{client_port}"
    print(f"Client connected: {client_id}")

    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received from {client_id}: {message}")
            await broadcast(message, sender=websocket)
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected: {client_id}")
    finally:
        connected_clients.remove(websocket)

async def broadcast(message: str, sender):
    for client in connected_clients:
        if client != sender:
            await client.send(message)
            client_ip, client_port = client.remote_address
            print(f"Broadcasted message to {client_ip}:{client_port}: {message}")

async def main():
    host, port = load_config('server')
    print(f"Starting WebSocket server on ws://{host}:{port}")
    async with websockets.serve(chat_server, host, port):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
