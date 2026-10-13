
from modules.machine_info import print_machine_info


def main():
    while True:
        print("=== Network Diagnostic and Tool Package ===")
        print("1. Machine Information")
        print("2. TCP Echo Test")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            print_machine_info()

        elif choice == "2":
            print("TCP Echo Test")
            print("Start the server in one terminal:")
            print("python modules/echo_test.py --port=9900")
            print("Then start the client in another terminal:")
            print("python modules/echo_client.py --port=9900")

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

