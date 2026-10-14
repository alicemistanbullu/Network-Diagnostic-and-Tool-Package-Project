
import socket
import argparse

host = "localhost"
data_payload = 2048
backlog = 5


def chat_server(port):
    """A simple TCP chat server."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)
    print("Starting chat server on %s port %s" % server_address)

    sock.bind(server_address)
    sock.listen(backlog)

    try:
        print("Waiting for a client...")
        client, address = sock.accept()
        print("Connected to", address)
        with open("logs/chat_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write("\n\n========== NEW CHAT ==========\n\n")
        print("Type 'exit' to end the chat.")

        with client:
            while True:
                data = client.recv(data_payload)

                if not data:
                    break

                message = data.decode("utf-8")
                print("Client: %s" % message)

                with open("logs/chat_log.txt", "a", encoding="utf-8") as log_file:
                    log_file.write("Client: " + message + "\n")

                if message.lower() == "exit":
                    break

                reply = input("You: ")

                with open("logs/chat_log.txt", "a", encoding="utf-8") as log_file:
                    log_file.write("Server: " + reply + "\n")

                client.sendall(reply.encode("utf-8"))

                if reply.lower() == "exit":
                    break

    except socket.error as error:
        print("Socket error: %s" % error)

    finally:
        sock.close()
        print("Chat server closed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Chat Server")
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()

    chat_server(args.port)

