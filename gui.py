
import os
import sys
import shutil
import subprocess
import threading
from pathlib import Path
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from modules.machine_info import print_machine_info
from modules.echo_runner import run_echo_test
from modules.ntp_time import print_time
from modules.sntp_time import sntp_client
from modules.error_management import (
    show_socket_settings,
    test_error_management
)


BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "logs" / "chat_log.txt"


class NetworkDiagnosticGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Network Diagnostic and Tool Package")
        self.root.geometry("1050x700")
        self.root.minsize(850, 600)

        self.busy = False

        # Configure the interface style
        style = ttk.Style()
        style.configure(
            "Tool.TButton",
            font=("Arial", 11),
            padding=(12, 10)
        )
        style.configure(
            "Footer.TButton",
            font=("Arial", 12, "bold"),
            padding=(16, 12)
        )

        # Main layout
        self.main_frame = ttk.Frame(root, padding=15)
        self.main_frame.pack(fill="both", expand=True)

        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Left menu
        self.menu_frame = ttk.LabelFrame(
            self.main_frame,
            text="Main Menu",
            padding=12
        )
        self.menu_frame.grid(
            row=0, column=0, sticky="ns", padx=(0, 15)
        )

        # Output area
        self.output_frame = ttk.LabelFrame(
            self.main_frame,
            text="Output",
            padding=10
        )
        self.output_frame.grid(
            row=0, column=1, sticky="nsew"
        )

        self.output_frame.rowconfigure(0, weight=1)
        self.output_frame.columnconfigure(0, weight=1)

        self.output = tk.Text(
            self.output_frame,
            wrap="word",
            font=("Consolas", 11),
            padx=10,
            pady=10,
            state="disabled"
        )
        self.output.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            self.output_frame,
            orient="vertical",
            command=self.output.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.output.configure(yscrollcommand=scrollbar.set)

        # Menu buttons in the same order as main.py
        self.add_menu_button(
            "1. Machine Information",
            lambda: self.run_task(print_machine_info)
        )
        self.add_menu_button(
            "2. TCP Echo Test",
            lambda: self.run_task(run_echo_test)
        )
        self.add_menu_button(
            "3. SNTP Time Check",
            self.open_sntp_menu
        )
        self.add_menu_button(
            "4. Simple Chat",
            self.open_chat_menu
        )
        self.add_menu_button(
            "5. Socket Settings and Error Management",
            self.open_socket_menu
        )

        ttk.Separator(
            self.menu_frame,
            orient="horizontal"
        ).pack(fill="x", pady=12)

        self.add_menu_button(
            "0. Exit",
            self.root.destroy
        )

        # Large bottom buttons
        self.footer = ttk.Frame(root, padding=(15, 0, 15, 15))
        self.footer.pack(fill="x")

        self.footer.columnconfigure(0, weight=1)
        self.footer.columnconfigure(1, weight=1)

        ttk.Button(
            self.footer,
            text="Clear Output",
            style="Footer.TButton",
            command=self.clear_output
        ).grid(row=0, column=0, sticky="ew", padx=(0, 8))

        ttk.Button(
            self.footer,
            text="Exit",
            style="Footer.TButton",
            command=self.root.destroy
        ).grid(row=0, column=1, sticky="ew", padx=(8, 0))

        self.write_output(
            "Welcome to Network Diagnostic and Tool Package.\n"
            "Select a tool from the main menu."
        )

    def add_menu_button(self, text, command):
        # Add a menu button
        button = ttk.Button(
            self.menu_frame,
            text=text,
            command=command,
            style="Tool.TButton"
        )
        button.pack(fill="x", pady=5)

    def write_output(self, text):
        # Display text in the output area
        self.output.configure(state="normal")
        self.output.insert("end", str(text) + "\n")
        self.output.see("end")
        self.output.configure(state="disabled")

    def clear_output(self):
        # Clear the output area
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")

    def run_task(self, function):
        # Prevent multiple tasks from running at once
        if self.busy:
            messagebox.showinfo(
                "Please wait",
                "Another task is still running."
            )
            return

        self.busy = True
        self.write_output("\nRunning task...\n")

        def task():
            buffer = StringIO()

            try:
                with redirect_stdout(buffer), redirect_stderr(buffer):
                    result = function()

                if result is not None:
                    buffer.write(f"\nResult: {result}\n")

            except Exception as error:
                buffer.write(f"\nError: {error}\n")

            text = buffer.getvalue()

            def finish():
                if text:
                    self.write_output(text)
                self.write_output("Task finished.\n")
                self.busy = False

            self.root.after(0, finish)

        threading.Thread(target=task, daemon=True).start()

    def open_sntp_menu(self):
        # Open the SNTP submenu
        window = tk.Toplevel(self.root)
        window.title("SNTP Time Check")
        window.geometry("350x220")
        window.resizable(False, False)

        ttk.Label(
            window,
            text="SNTP Time Check",
            font=("Arial", 14, "bold")
        ).pack(pady=12)

        ttk.Button(
            window,
            text="1. Use ntplib",
            style="Tool.TButton",
            command=lambda: self.run_task(print_time)
        ).pack(fill="x", padx=20, pady=5)

        ttk.Button(
            window,
            text="2. Use socket",
            style="Tool.TButton",
            command=lambda: self.run_task(sntp_client)
        ).pack(fill="x", padx=20, pady=5)

    def open_chat_menu(self):
        # Open the Simple Chat submenu
        window = tk.Toplevel(self.root)
        window.title("Simple Chat")
        window.geometry("350x250")
        window.resizable(False, False)

        ttk.Label(
            window,
            text="Simple Chat",
            font=("Arial", 14, "bold")
        ).pack(pady=12)

        ttk.Button(
            window,
            text="1. Start Chat Server",
            style="Tool.TButton",
            command=lambda: self.start_chat("chat_server")
        ).pack(fill="x", padx=20, pady=5)

        ttk.Button(
            window,
            text="2. Start Chat Client",
            style="Tool.TButton",
            command=lambda: self.start_chat("chat_client")
        ).pack(fill="x", padx=20, pady=5)

        ttk.Button(
            window,
            text="3. View Chat Logs",
            style="Tool.TButton",
            command=self.view_chat_logs
        ).pack(fill="x", padx=20, pady=5)

    def start_chat(self, module_name):
        # Ask for the chat port
        port = simpledialog.askinteger(
            "Chat Port",
            "Enter port number (e.g. 9901):",
            parent=self.root,
            minvalue=1,
            maxvalue=65535
        )

        if port is None:
            return

        command = [
            sys.executable,
            "-m",
            f"modules.{module_name}",
            "--port",
            str(port)
        ]

        # Open the chat program in a separate console
        try:
            if os.name == "nt":
                subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)

            else:
                terminal = shutil.which("x-terminal-emulator")

                if terminal:
                    subprocess.Popen([terminal, "-e", *command])
                else:
                    messagebox.showinfo(
                        "Chat",
                        "No terminal emulator was found.\n"
                        "Run the chat module from a separate terminal:\n\n"
                        + " ".join(command)
                    )

        except OSError as error:
            messagebox.showerror("Chat Error", str(error))

    def view_chat_logs(self):
        # Display saved chat logs
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as file:
                logs = file.read()

            if logs:
                self.write_output("\n=== Chat Logs ===\n" + logs)
            else:
                self.write_output("Chat log file is empty.")

        except FileNotFoundError:
            self.write_output("No chat log file found yet.")

    def open_socket_menu(self):
        # Open the socket settings submenu
        window = tk.Toplevel(self.root)
        window.title("Socket Settings and Error Management")
        window.geometry("420x220")
        window.resizable(False, False)

        ttk.Label(
            window,
            text="Socket Settings and Error Management",
            font=("Arial", 12, "bold"),
            wraplength=380
        ).pack(pady=12)

        ttk.Button(
            window,
            text="1. Socket Settings",
            style="Tool.TButton",
            command=lambda: self.run_task(show_socket_settings)
        ).pack(fill="x", padx=20, pady=5)

        ttk.Button(
            window,
            text="2. Test Connection Error Handling",
            style="Tool.TButton",
            command=lambda: self.run_task(test_error_management)
        ).pack(fill="x", padx=20, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkDiagnosticGUI(root)
    root.mainloop()
