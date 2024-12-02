#!/usr/bin/env python3

import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def install_figlet():
    """Ensure figlet is installed."""
    subprocess.run(["apt-get", "install", "figlet", "-y"], check=True)
    subprocess.run(["clear"])
    subprocess.run(["figlet", "NMAP TOOL"])


def print_menu():
    """Display the menu to the user with color."""
    print(Fore.CYAN + Style.BRIGHT + """
[1] Full system analysis with OS and version detection
[2] Scan with default and aggressive scripts
[3] Vulnerability scan with detailed script output
[4] Fragmented IP packet scan
[5] Scan only open ports
[6] Scan multiple targets (target1,target2,...)
[7] Use stealth SYN scan
[8] Perform a ping sweep
""")


def get_user_input():
    """Get user inputs for scan type, destination IP, and scan speed."""
    try:
        choice = int(input(Fore.GREEN + "Select an option (1-8): ").strip())
        if choice not in range(1, 9):
            raise ValueError("Invalid menu choice")
    except ValueError:
        print(Fore.RED + "Invalid choice. Please select a valid option (1-8).")
        return None, None, None

    dst = input(Fore.YELLOW + "Enter the destination IP address or range: ").strip()
    ttt = input(Fore.YELLOW + "Enter scan speed (0-5, recommended=4): ").strip()
    
    if not ttt.isdigit() or not (0 <= int(ttt) <= 5):
        print(Fore.RED + "Invalid scan speed. Please enter a number between 0 and 5.")
        return None, None, None

    return choice, dst, ttt


def execute_nmap(choice, dst, ttt):
    """Run the nmap command based on user choice."""
    commands = {
        1: ["nmap", dst, f"-T{ttt}", "-A"],
        2: ["nmap", dst, f"-T{ttt}", "-sC", "-sV"],
        3: ["nmap", dst, f"-T{ttt}", "--script", "vuln"],
        4: ["nmap", dst, "-f"],
        5: ["nmap", dst, "-Pn", f"-T{ttt}"],
        6: ["nmap", dst, f"-T{ttt}"],
        7: ["nmap", dst, f"-T{ttt}", "-sS"],
        8: ["nmap", dst, "-sn"],
    }

    command = commands.get(choice)
    if command:
        print(Fore.MAGENTA + "Executing: " + " ".join(command))
        subprocess.run(command)
    else:
        print(Fore.RED + "An unexpected error occurred.")


def main():
    install_figlet()
    print_menu()
    
    choice, dst, ttt = get_user_input()
    if choice and dst and ttt:
        execute_nmap(choice, dst, ttt)
    else:
        print(Fore.RED + "Restarting...")
        main()


if __name__ == "__main__":
    main()
