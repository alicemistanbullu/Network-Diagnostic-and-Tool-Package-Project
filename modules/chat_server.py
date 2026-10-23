import socket
import argparse
from datetime import datetime

host = "localhost"
data_payload = 2048  # Set the maximum data size
backlog = 5  # Set the connection queue size


def chat_server(port):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)  # Set server address and port
    print("Starting chat server on %s port %s" % server_address)

    sock.bind(server_address)  # Bind the socket
    sock.listen(backlog)  # Wait for client connections

    try:
        print("Waiting for a client...")
        client, address = sock.accept()  # Accept a client connection
        print("Connected to", address)

        # Mark the beginning of a new chat session
        with open("logs/chat_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write("\n\n========== NEW CHAT ==========\n\n")

        print("Type 'exit' to end the chat.")

        with client:
            while True:
                data = client.recv(data_payload)  # Receive client message

                if not data:
                    break

                message = data.decode("utf-8")  # Convert bytes to text
                print("Client: %s" % message)
                log_message("Client", message)  # Save the message

                if message.lower() == "exit":
                    break

                reply = input("You: ")  # Enter a reply
                log_message("Server", reply)  # Save the reply
                client.sendall(reply.encode("utf-8"))  # Send the reply

                if reply.lower() == "exit":
                    break

    except socket.error as error:
        print("Socket error: %s" % error)

    finally:
        sock.close()  # Close the server socket
        print("Chat server closed.")


def log_message(sender, message):
    # Get the current date and time
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")

    # Save the message to the log file
    with open("logs/chat_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {sender}: {message}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Chat Server")
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()

    chat_server(args.port)  # Start the chat server
