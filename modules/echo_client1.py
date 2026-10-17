
import socket
import time
import argparse

host = "localhost"


def echo_client(port):
    """Send a test message and verify the echo response."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)

    message = "Test message. This will be echoed"
    start_time = time.time()

    try:
        sock.settimeout(3.0)

        print("Connecting to %s port %s" % server_address)
        sock.connect(server_address)

        print("Sending:", message)
        sock.sendall(message.encode("utf-8"))

        received_data = b""

        while len(received_data) < len(message.encode("utf-8")):
            data = sock.recv(2048)

            if not data:
                break

            received_data += data

        received_message = received_data.decode("utf-8", errors="replace")
        duration = time.time() - start_time

        success = received_data == message.encode("utf-8")

        print("Received:", received_message)
        print("Duration: %.4f seconds" % duration)

        if success:
            print("Echo test PASSED: data matches.")
        else:
            print("Echo test FAILED: data does not match.")

        return {
            "success": success,
            "sent_message": message,
            "received_message": received_message,
            "duration": duration,
            "error": None
        }

    except (socket.timeout, OSError) as error:
        duration = time.time() - start_time
        print("Echo test FAILED:", error)

        return {
            "success": False,
            "sent_message": message,
            "received_message": "",
            "duration": duration,
            "error": str(error)
        }

    finally:
        sock.close()
        print("Connection closed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Echo Client")
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()

    echo_client(args.port)
