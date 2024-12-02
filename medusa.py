#!/usr/bin/env python3

import subprocess
from colorama import Fore, Style, init
import datetime

# Initialize colorama
init(autoreset=True)

def install_figlet():
    """Ensure figlet is installed."""
    subprocess.run(["apt-get", "install", "figlet", "-y"], check=True)
    subprocess.run(["clear"])
    subprocess.run(["figlet", "MEDUSA TOOL"])


def print_menu():
    """Display the menu to the user."""
    print(Fore.CYAN + Style.BRIGHT + """
[1] Brute-force SSH
[2] Brute-force FTP
[3] Brute-force HTTP
[4] Brute-force MySQL
[5] Brute-force SMB
[6] Brute-force VNC
[7] Custom Medusa Command
""")


def get_user_input():
    """Get user inputs for attack type and target details."""
    try:
        choice = int(input(Fore.GREEN + "Select an option (1-7): ").strip())
        if choice not in range(1, 8):
            raise ValueError("Invalid menu choice")
    except ValueError:
        print(Fore.RED + "Invalid choice. Please select a valid option (1-7).")
        return None, None, None, None

    target = input(Fore.YELLOW + "Enter the target IP or domain: ").strip()
    username = input(Fore.YELLOW + "Enter the username: ").strip()
    password_file = input(Fore.YELLOW + "Enter the path to the password file: ").strip()

    return choice, target, username, password_file


def log_results(command, output):
    """Log the Medusa results to a file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"medusa_scan_{timestamp}.log"
    with open(log_filename, "w") as log_file:
        log_file.write(f"Command: {' '.join(command)}\n")
        log_file.write(output)
    print(Fore.GREEN + f"Results saved to {log_filename}")


def execute_medusa(choice, target, username, password_file):
    """Run the Medusa command based on user choice."""
    protocols = {
        1: "ssh",
        2: "ftp",
        3: "http",
        4: "mysql",
        5: "smbnt",
        6: "vnc",
    }

    if choice in protocols:
        command = [
            "medusa",
            "-h", target,
            "-u", username,
            "-P", password_file,
            "-M", protocols[choice],
        ]
    elif choice == 7:
        command = input(Fore.MAGENTA + "Enter your custom Medusa command: ").strip().split()
    else:
        print(Fore.RED + "Invalid option.")
        return

    print(Fore.MAGENTA + "Executing: " + " ".join(command))
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    log_results(command, result.stdout)


def main():
    install_figlet()
    print_menu()

    choice, target, username, password_file = get_user_input()
    if choice and target and username and password_file:
        execute_medusa(choice, target, username, password_file)
    else:
        print(Fore.RED + "Restarting...")
        main()


if __name__ == "__main__":
    main()
