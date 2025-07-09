import socket
import sys
import time
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

available_ports = []

def init(ip_address):
    print(f"Initializing connection to {ip_address}")
    for i in range(65536):
        print(f"Connecting to port {i}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            if s.connect_ex((ip_address, i)) == 0 :
                print(f"Connected to {ip_address} on port {i}")
                print(f"Port {i} is available.")
                available_ports.append(i)
            s.close()
        except socket.error as e:
            print(f"Failed to connect to {ip_address} on port {i}: {e}")
            print(f"Port {i} is not available.")
        finally:
            s.close()
    print("Initialization complete.")

if __name__ == "__main__":
    if len(sys.argv) == 2 :
        if is_valid_ip(sys.argv[1]):
            ip_address = sys.argv[1]
        else:
            print("Invalid IP address format. Please provide a valid IP address.")
            sys.exit(1)
    else:
        print("No IP address provided. Please provide an IP address as a command line argument.")
        print("Example: python script.py 0000.000.000.000")
        sys.exit(1)
    print("Starting the script...")
    init_time = time.time()
    init(ip_address)
    print(f"Available ports on {ip_address}: {available_ports}")
    print("Script finished running.")
    end_time = time.time()
    print(f"Total time taken: {end_time - init_time} seconds")
    print("You can now use the script to check port availability.")
    print("Note: This script will attempt to connect to every port from 0 to 65535.")
    print("This may take a while depending on the number of ports and network conditions.")
    print("Make sure you have the necessary permissions to scan ports on the target IP address.")
    print("Use this script responsibly and in accordance with local laws and regulations.")