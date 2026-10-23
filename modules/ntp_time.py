import ntplib  # Import the NTP library
from time import ctime  # Import a function to format time

def print_time():
    # Create an NTP client
    ntp_client = ntplib.NTPClient()

    # Send a request to the NTP server
    response = ntp_client.request('pool.ntp.org')
    print(ctime(response.tx_time))

if __name__ == '__main__':
    print_time()
