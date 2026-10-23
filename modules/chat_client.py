import socket
import argparse

host = "localhost"
data_payload = 2048 #Set the max data size

def chat_client(port):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)  # Set server address and port
    print("Connecting to %s port %s" % server_address)

    try:
        sock.connect(server_address)  # Connect to the server
        print("Connected to chat server.")
        print("Type 'exit' to end the chat.")

        while True:
            message = input("You: ")  # Get a message from the user
            sock.sendall(message.encode("utf-8"))  # Send the message

            if message.lower() == "exit":
                break

            data = sock.recv(data_payload)  # Receive the server reply

            if not data:
                print("Server disconnected.")
                break

            reply = data.decode("utf-8")  # Convert bytes to text
            print("Server: %s" % reply)

            if reply.lower() == "exit":
                break

    except socket.error as error:
        print("Socket error: %s" % error)

    finally:
        sock.close()
        print("Connection closed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Chat Client")
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()

    chat_client(args.port)  # Start the chat client
