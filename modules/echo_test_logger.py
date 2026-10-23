import os
from datetime import datetime
import ntplib
from time import ctime

def get_network_time():
    try:
        # Request the current time from an NTP server
        client = ntplib.NTPClient()
        response = client.request("pool.ntp.org", timeout=3)

        # Convert the timestamp to readable time
        return ctime(response.tx_time)

    except Exception as error:
        print("Could not get network time:", error)
        return None


def save_echo_result(result, duration):
    # Get the current local time
    local_time = datetime.now().astimezone().isoformat(timespec="seconds")

    # Get the network time
    network_time = get_network_time()

    # Create the logs folder if it does not exist
    os.makedirs("logs", exist_ok=True)

    # Open the log file in append mode
    with open("logs/echo_test_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write("\n========== TCP ECHO TEST ==========\n")

        # Save the test status
        log_file.write("Status: %s\n" %("PASSED" if result["success"] else "FAILED"))

        # Save the sent and received messages
        log_file.write("Sent message: %s\n" % result["sent_message"])
        log_file.write("Received message: %s\n" % result["received_message"])

        # Save any error information
        log_file.write("Error: %s\n" % (result["error"] or "None"))

        # Save local and network times
        log_file.write("Local time: %s\n" % local_time)
        log_file.write("NTP time: %s\n" %(network_time if network_time else "Unavailable"))

        # Save the test duration
        log_file.write("Duration: %.4f seconds\n" % duration)
        log_file.write("===================================\n")

    print("Echo test result saved to logs/echo_test_log.txt")
