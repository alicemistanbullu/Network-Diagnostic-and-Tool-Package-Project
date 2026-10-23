import socket  # Import the socket module


def show_socket_settings():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        #Display the default socket settings
        print("\n=== Socket Settings ===")
        print("Default timeout:", sock.gettimeout())
        print("Default blocking mode:", sock.getblocking())
        print("Default send buffer:", sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
        print("Default receive buffer:", sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))

        # Set the socket timeout to 3 seconds
        sock.settimeout(3.0)

        # Set the send and receive buffer sizes
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)

        # Display the updated socket settings
        print("\n--- Updated Settings ---")
        print("Timeout:", sock.gettimeout())
        print("Blocking mode:", sock.getblocking())
        print("Send buffer:", sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
        print("Receive buffer:", sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))

        # Enable non-blocking mode
        sock.setblocking(False)
        print("Blocking mode after change:", sock.getblocking())
        print("\nSocket settings demonstration completed.")

def test_error_management():
    print("\n=== Error Management ===")

    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            # Set the connection timeout to 3 seconds
            sock.settimeout(3.0)

            # Try to connect to the local port 9999
            print("Connecting to 127.0.0.1:9999")
            sock.connect(("127.0.0.1", 9999))
            print("Connection successful.")

    except socket.timeout:
        print("Error: Connection timed out.")

    except ConnectionRefusedError:
        print("Error: Connection refused. No server is listening.")

    except OSError as error:
        print("Socket error:", error)

    finally:
        print("Connection test finished.")

if __name__ == "__main__":
    show_socket_settings()
    test_error_management()
