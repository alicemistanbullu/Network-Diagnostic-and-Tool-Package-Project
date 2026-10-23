import socket
import time
import argparse

host = "localhost"


def echo_client(port):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)  # Set server address and port

    message = "Test message. This will be echoed"
    start_time = time.time()  # Start measuring time

    try:
        sock.settimeout(3.0)  # Set connection timeout

        print("Connecting to %s port %s" % server_address)
        sock.connect(server_address)  # Connect to the server

        print("Sending:", message)
        sock.sendall(message.encode("utf-8"))  # Send the test message

        received_data = b""

        # Receive data until the full message arrives
        while len(received_data) < len(message.encode("utf-8")):
            data = sock.recv(2048)

            if not data:
                break

            received_data += data

        received_message = received_data.decode("utf-8", errors="replace")
        duration = time.time() - start_time  # Calculate test duration

        # Check if the received message matches the sent message
        success = received_data == message.encode("utf-8")

        print("Received:", received_message)
        print("Duration: %.4f seconds" % duration)

        if success:
            print("Echo test PASSED: data matches.")
        else:
            print("Echo test FAILED: data does not match.")

        # Return the test results
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

        # Return the error information
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

    echo_client(args.port)  # Start the echo test
