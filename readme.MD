This project demonstrates a simple WebSocket websocket server and client. 
The client script sends timestamp messages every second, and the server broadcasts these messages to all other connected clients (eg Resonite).

---

## Project Structure

```

resonite-boilerplate-scripts/
├── ws_server.py           # WebSocket server
├── ws_client.py           # WebSocket client
├── helpers.py             # Loads configuration from config.ini
├── config.ini             # Your actual config file (you create this)
├── config_sample.ini      # Template config file
└── requirements.txt       # Python dependencies

````

---

## Prerequisites

- Python 3.10 or newer

---

## Installation

1. **Clone or download this repository**.

2. **Install the required Python packages** using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

This only needs to be done once.

---

## Configuration

Before running the server or client, you must create a config file.

### 1. Create `config.ini`

Make a copy of the `config_sample.ini` file named `config.ini` in the same directory.

Identify your local IP address. Run:

* `ipconfig` on **Windows**
* `ifconfig` on **Linux/macOS**

Then edit `config.ini` and adjust IP and port values. When getting started, the server and client sections will be the same.

For example:

```ini
[server]
host = 10.0.0.106
port = 8765

[client]
host = 10.0.0.106
port = 8765
```


---

## Running the Server script

```bash
python ws_server.py
```

---

## Running the Client script

```bash
python ws_client.py
```

---

## How It Works

* **Server:** Accepts connections from any number of clients and broadcasts received messages to all other clients.
* **Client:** Sends the current Unix timestamp every 1 second to the server.
* **All clients receive all messages** (except their own).


This means if you run the server and client scripts, you can connect to the websocket server on Resonite and see the messages sent by the client.

---

## Connecting to websocket server via Resonite

1. Spawn this public folder by pasting the following link into Resonite:
`resrec:///U-DingoYabuki/R-9793cb26-f9ac-4eea-b52d-1bafdff8e502`
2. Open your Inventory, navigate to the folder, and spawn item `/Protoflux Snippets/Websocket Demo/WebsocketClientExample`
3. Unpack the `WebsocketClientExample/Protoflux/WebsocketClientProtoflux` slot
4. Modify the `Uri input` field with your websocket server IP and port, eg `ws://10.0.0.106:8765`
5. Click the "Call" trigger on the `Websocket Connect` protoflux node
6. If the server and client are running, you should see the `LatestReceivedWebsocketMessage` variable update with the timestamp sent by the client script every second.

![Protoflux WebSocket Setup](screenshots/Protoflux.png)