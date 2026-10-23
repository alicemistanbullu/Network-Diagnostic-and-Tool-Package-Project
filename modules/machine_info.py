import socket  # Import the socket module

def print_machine_info():
    # Get the computer's host name
    host_name = socket.gethostname()

    print("\n=== Machine Information ===")
    print("Host name:", host_name)

    try:
        # Get the IP address using the host name
        ip_address = socket.gethostbyname(host_name)
        print("IP address:", ip_address)

    except socket.gaierror as error:
        # Display an error if the IP address can't be found
        print("Could not get IP address:", error)

    print("\n=== Network Interfaces ===")

    # Get the available network interfaces
    interfaces = socket.if_nameindex()

    # Print each network interface name
    if interfaces:
        for index, name in interfaces:
            print("Interface:", name)
    else:
        print("No network interfaces found.")

if __name__ == "__main__":
    print_machine_info()
