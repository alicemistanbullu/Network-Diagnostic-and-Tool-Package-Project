
import socket


def print_machine_info():

    host_name = socket.gethostname()

    print("\n=== Machine Information ===")
    print("Host name:", host_name)

    try:
        ip_address = socket.gethostbyname(host_name)
        print("IP address:", ip_address)

    except socket.gaierror as error:
        print("Could not get IP address:", error)

    print("\n=== Network Interfaces ===")

    interfaces = socket.if_nameindex()

    if interfaces:
        for index, name in interfaces:
            print("Interface:", name)
    else:
        print("No network interfaces found.")


if __name__ == "__main__":
    print_machine_info()

