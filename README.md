
**Course:** CEN322 – Network Programming
**Project:** Network Diagnostic and Tool Package

## Overview

This Python application combines basic network diagnostics and socket programming examples in one program. It includes machine information, an automatic TCP Echo Test, SNTP time checking, a simple TCP chat, and socket settings and error management demonstrations.

## Features

- **Machine Information:** Displays the machine hostname, IP address, and available network interfaces.
- **TCP Echo Test:** Starts a local echo server automatically, sends a test message, compares the sent and received data, measures the duration, and records the result.
- **SNTP Time Check:** Retrieves network time using either `ntplib` or raw UDP socket.
- **Simple Chat:** Runs a chat server or client and records chat messages with timestamps. The GUI also provides an option to view saved chat logs.
- **Socket Settings and Error Management:** Demonstrates timeout, send/receive buffer sizes, blocking/non-blocking mode, and connection-error handling.

## Requirements

- Python 3
- `ntplib`
- Tkinter

## Setup

Open a terminal in the project directory and activate your virtual environment.

On Linux / WSL:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

If Tkinter is not installed on Ubuntu / Debian:

```bash
sudo apt update
sudo apt install python3-tk
```

If the virtual environment already exists, activate it and install the requirements:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the application

From the project root directory, run:

```bash
python gui.py
```

Select a tool from the graphical interface.

## Simple Chat

The chat server and client run as separate processes launched from the GUI.

- Select **Simple Chat → Start Chat Server** and enter a port such as `9901`.
- Select **Simple Chat → Start Chat Client** and enter the same port.
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
├── gui.py
├── modules/
│   ├── __init__.py
│   ├── machine_info.py
│   ├── echo_client.py
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
