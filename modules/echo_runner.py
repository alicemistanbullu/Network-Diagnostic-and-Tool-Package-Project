
import socket
import time
import threading
from modules.echo_client1 import echo_client
from modules.echo_test_logger import save_echo_result

def run_echo_test():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", 0))
    server.listen(1)

    port = server.getsockname()[1]

    def handle_client():
        try:
            client, address = server.accept()

            with client:
                print("Echo server connected to:", address)

                data = client.recv(2048)

                if data:
                    client.sendall(data)

        except OSError as error:
            print("Echo server error:", error)

        finally:
            server.close()

    server_thread = threading.Thread(target=handle_client)
    server_thread.start()

    print("\n=== Automatic TCP Echo Test ===")
    start_time = time.time()
    result = echo_client(port)
    duration = time.time() - start_time
    save_echo_result(result, duration)
    server_thread.join(timeout=4)

    return result


if __name__ == "__main__":
    run_echo_test()

