**Course:** CEN322 – Network Programming
**Project:** Network Diagnostic and Tool Package

## Overview

This Python application combines basic network diagnostics and socket programming examples in one program. It includes machine information, an automatic TCP Echo Test, SNTP time checking, a simple TCP chat, and socket settings and error management demonstrations.

## Features

- **Machine Information:** Displays the machine hostname, IP address, and available network interfaces.
- **TCP Echo Test:** Starts a local echo server automatically, sends a test message, compares the sent and received data, measures the duration, and records the result.
- **SNTP Time Check:** Retrieves network time using either `ntplib` or raw UDP socket.
- **Simple Chat:** Runs a chat server or client and records chat messages with timestamps. The menu also provides an option to view saved chat logs.
- **Socket Settings and Error Management:** Demonstrates timeout, send/receive buffer sizes, blocking/non-blocking mode, and connection-error handling.

## Requirements

- Python 3
- `ntplib` (the only third-party Python dependency)

The other modules use Python's standard library.

## Setup

Open a terminal in the project directory and activate your virtual environment.

On Linux / WSL:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

If the virtual environment already exists, activate it and install the requirements:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the application

From the project root directory:

```bash
python main.py
```

Follow the on-screen menu to select a module.

### Simple Chat

The chat server and client need separate processes. Open two terminals in the same project directory, activate the virtual environment in both, and run `python main.py` in each terminal.

- In the first terminal, select **Simple Chat → Start Chat Server** and enter a port such as `9901`.
- In the second terminal, select **Simple Chat → Start Chat Client** and enter the same port.
- Exchange messages. Enter `exit` to end the chat.

The current chat implementation uses `localhost`, so both processes should run on the same machine.

## Logs

The application writes runtime logs under the `logs/` directory:

- `logs/echo_test_log.txt` — echo test status, sent/received message, error, NTP timestamp, and duration.
- `logs/chat_log.txt` — chat messages with timestamps.


## Project structure

```text
NetworkProgramming-1/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── machine_info.py
│   ├── echo_client.py / echo_client1.py
│   ├── echo_test.py
│   ├── echo_runner.py
│   ├── echo_test_logger.py
│   ├── ntp_time.py
│   ├── sntp_time.py
│   ├── chat_server.py
│   ├── chat_client.py
│   └── error_management.py
├── logs/
│   ├── .gitkeep
│   ├── echo_test_log.txt
│   └── chat_log.txt   
├── requirements.txt
└── README.md
```
