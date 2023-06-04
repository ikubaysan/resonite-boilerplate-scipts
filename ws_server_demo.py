# To run:
# 1. Install Python 3
# In command prompt:
# 2. run "pip install websockets asyncio"  (only need to do this once, this installs the dependencies needed to run the script)
# 3. run "python ws_server_demo.py" in the folder containing the this file

import asyncio
import websockets

connected_clients = set()

async def chat_server(websocket, path):
    server_address = websocket.remote_address[0] + ":" + str(websocket.remote_address[1])
    print(f"Client connected from {server_address}")

    try:
        connected_clients.add(websocket)

        while True:
            received_message = await websocket.recv()
            print(f"Received message '{received_message}' from {server_address}")

            for client in connected_clients:
                await client.send(received_message)
                print(f"Broadcasted message '{received_message}' to {client.remote_address[0]}:{client.remote_address[1]}")

    except websockets.exceptions.ConnectionClosed:
        print(f"Client {server_address} disconnected")
        connected_clients.remove(websocket)

# Enter your local IP address, which you can find using the "ipconfig" command
server_address = '10.0.0.106'
server_port = 8765

start_server = websockets.serve(chat_server, server_address, server_port)

print(f"Server is running at ws://{server_address}:{server_port}")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
