# WebSocket Chat Demo (Python)

This project demonstrates a simple WebSocket-based chat server and client using Python's `asyncio` and the `websockets` library. 
The server is connectable from Resonite.

## Requirements

Python 3.10 or higher

# Getting Started

## Install the Dependencies
You only need to install the dependencies once. Open a terminal or command prompt in this repository's folder and run:

```bash
pip install -r requirements.txt
```

## Running the Server

1. Open `ws_server.py` and set your local IP address (e.g., `10.0.0.106`).
   You can find your IP using:

   ```bash
   ipconfig   # on Windows
   ifconfig   # on Mac/Linux
   ```
2. Start the server:

   ```bash
   python ws_server.py
   ```

## 📡 Running the Client

1. Ensure the IP in `ws_client.py` matches the server's IP.
2. Run the client:

   ```bash
   python ws_client.py
   ```

## What it does

* The server receives messages from all connected clients and broadcasts them to all others.
* The client sends a Unix timestamp every second to the server.

You will be able to connect to the websocket server in Resonite, run the ws_client script, and see a message appear in-game every second.

Use


## 📎 Notes

* Both files must be run from the same local network.
* This is a basic demo without SSL or authentication—do not use in production as-is.

```