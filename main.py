
from modules.machine_info import print_machine_info
from modules.sntp_time import sntp_client
from modules.ntp_time import print_time

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

def main():
    while True:
        print("\n=== Network Diagnostic and Tool Package ===")
        print("1. Machine Information")
        print("2. TCP Echo Test")
        print("3. SNTP Time Check")
        print("0. Exit\n")

        choice = input("Select an option: ")

        if choice == "1":
            print_machine_info()

        elif choice == "2":
            print("TCP Echo Test")
            print("Start the server in one terminal:")
            print("python modules/echo_test.py --port=9900")
            print("Then start the client in another terminal:")
            print("python modules/echo_client.py --port=9900")

        elif choice == "3":
            sntp_menu()

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

