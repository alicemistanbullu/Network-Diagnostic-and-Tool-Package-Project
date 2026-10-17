
import socket


def show_socket_settings():
    """Display and demonstrate basic socket settings."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("\n=== Socket Settings ===")

        # Display default settings
        print("Default timeout:", sock.gettimeout())
        print("Default blocking mode:", sock.getblocking())
        print("Default send buffer:", sock.getsockopt(
            socket.SOL_SOCKET, socket.SO_SNDBUF
        ))
        print("Default receive buffer:", sock.getsockopt(
            socket.SOL_SOCKET, socket.SO_RCVBUF
        ))

        # Set timeout to 3 seconds
        sock.settimeout(3.0)

        # Set send and receive buffer sizes
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)

        print("\n--- Updated Settings ---")
        print("Timeout:", sock.gettimeout())
        print("Blocking mode:", sock.getblocking())
        print("Send buffer:", sock.getsockopt(
            socket.SOL_SOCKET, socket.SO_SNDBUF
        ))
        print("Receive buffer:", sock.getsockopt(
            socket.SOL_SOCKET, socket.SO_RCVBUF
        ))

        # Demonstrate non-blocking mode
        sock.setblocking(False)
        print("Blocking mode after change:", sock.getblocking())

        print("\nSocket settings demonstration completed.")


def test_error_management():
    """Demonstrate timeout and socket error handling."""

    print("\n=== Error Management ===")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(3.0)

            print("Connecting to 127.0.0.1:9999...")
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
