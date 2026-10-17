
from modules.machine_info import print_machine_info
from modules.sntp_time import sntp_client
from modules.ntp_time import print_time
from modules.chat_server import chat_server
from modules.chat_client import chat_client
from modules.error_management import (show_socket_settings, test_error_management)
from modules.echo_runner import run_echo_test

def sntp_menu():
    while True:
        print("\n=== SNTP Time Check ===")
        print("1. Use ntplib")
        print("2. Use socket")
        print("0. Back to main menu\n")

        choice = input("Select an option: ")

        if choice == "1":
            print("Using ntplib...")
            print_time()

        elif choice == "2":
            print("Using socket...")
            network_time = sntp_client()

            if network_time:
                print(f"Network time: ")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def chat_menu():
    while True:
        print("\n=== Simple Chat ===")
        print("1. Start Chat Server")
        print("2. Start Chat Client")
        print("3. View Chat Logs")
        print("0. Back to Main Menu\n")

        choice = input("Select an option: ")

        if choice == "1":
            port = int(input("Enter port number (e.g. 9901): "))
            chat_server(port)

        elif choice == "2":
            port = int(input("Enter port number (e.g. 9901): "))
            chat_client(port)

        elif choice == "3":
            view_chat_logs()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

def view_chat_logs():
    log_file = "logs/chat_log.txt"

    try:
        with open(log_file, "r", encoding="utf-8") as file:
            logs = file.read()

        if logs:
            print("\n===Chat Logs===")
            print(logs)

        else:
            print("Chat log file is empty.")

    except FileNotFoundError:
        print("No chat file found yet.")

def error_management_menu():
    while True:
        print("\n===Socket Settings and Error Management===")
        print("1. Socket Settings")
        print("2. Test Connection Error Handling")
        print("0. Exit\n")

        choice = input("Select an option: ")

        if choice == "1":
            show_socket_settings()

        elif choice == "2":
            test_error_management()

        elif choice == "0":
            break

        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        print("\n=== Network Diagnostic and Tool Package ===")
        print("1. Machine Information")
        print("2. TCP Echo Test")
        print("3. SNTP Time Check")
        print("4. Simple Chat")
        print("5. Socket Settings and Error Management")
        print("0. Exit\n")

        choice = input("Select an option: ")

        if choice == "1":
            print_machine_info()

        elif choice == "2":
            run_echo_test()

        elif choice == "3":
            sntp_menu()

        elif choice == "4":
            chat_menu()

        elif choice == "5":
            error_management_menu()

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

