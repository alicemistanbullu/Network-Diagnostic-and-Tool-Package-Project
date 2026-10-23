import socket
import struct
import time

# Define the NTP server address
NTP_SERVER = "0.uk.pool.ntp.org"

# Store the difference between 1900 and 1970 in seconds
TIME1970 = 2208988800

def sntp_client():
    # Create a UDP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Create an SNTP request message
    data = b'\x1b' + 47 * b'\0'

    # Send the request to the NTP server on port 123
    client.sendto(data, (NTP_SERVER, 123))

    # Receive the server response
    data, address = client.recvfrom(1024)

    # Display the server address if data is received
    if data:
        print('Response received from:', address)

    # Extract the timestamp from the response
    t = struct.unpack('!12I', data)[10]

    # Convert the timestamp to Unix time
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))

if __name__ == '__main__':
    sntp_client()
