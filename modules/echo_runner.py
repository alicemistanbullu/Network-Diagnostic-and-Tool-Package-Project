import socket
import time
import threading
from modules.echo_client import echo_client
from modules.echo_test_logger import save_echo_result

def run_echo_test():
    # Create a TCP server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to an available local port
    server.bind(("localhost", 0))
    server.listen(1)

    # Get the assigned port number
    port = server.getsockname()[1]

    def handle_client():
        try:
            # Wait for the client connection
            client, address = server.accept()

            with client:
                print("Echo server connected to:", address)

                # Receive and return the client's message
                data = client.recv(2048)

                if data:
                    client.sendall(data)

        except OSError as error:
            print("Echo server error:", error)

        finally:
            server.close()  # Close the server socket

    # Start the server in a separate thread
    server_thread = threading.Thread(target=handle_client)
    server_thread.start()

    print("\n=== Automatic TCP Echo Test ===")

    # Run the client and measure the duration
    start_time = time.time()
    result = echo_client(port)
    duration = time.time() - start_time

    # Save the test result
    save_echo_result(result, duration)

    # Wait for the server thread to finish
    server_thread.join(timeout=4)
    return result

if __name__ == "__main__":
    run_echo_test()
