
import os
from datetime import datetime
import ntplib
from time import ctime


def get_network_time():

    try:
        client = ntplib.NTPClient()
        response = client.request("pool.ntp.org", timeout=3)
        return ctime(response.tx_time)

    except Exception as error:
        print("Could not get network time:", error)
        return None


def save_echo_result(result, duration):

    local_time = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )
    network_time = get_network_time()

    os.makedirs("logs", exist_ok=True)

    with open("logs/echo_test_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write("\n========== TCP ECHO TEST ==========\n")
        log_file.write(
            "Status: %s\n" %
            ("PASSED" if result["success"] else "FAILED")
        )
        log_file.write("Sent message: %s\n" % result["sent_message"])
        log_file.write(
            "Received message: %s\n" % result["received_message"]
        )
        log_file.write("Error: %s\n" % (result["error"] or "None"))
        log_file.write("Local time: %s\n" % local_time)
        log_file.write(
            "NTP time: %s\n" %
            (network_time if network_time else "Unavailable")
        )
        log_file.write("Duration: %.4f seconds\n" % duration)
        log_file.write("===================================\n")

    print("Echo test result saved to logs/echo_test_log.txt")
