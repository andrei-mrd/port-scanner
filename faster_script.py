import socket
import sys
import time
from concurrent.futures import ProcessPoolExecutor
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def init(ip_address, start_port, end_port):
    local_available_ports = []
    for i in range(start_port, end_port + 1):
        print(f"Connecting to port {i}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)  # Set a timeout for the connection attempt

        if s.connect_ex((ip_address, i)) == 0:
            local_available_ports.append(i)
        s.close()

    print("Initialization complete.")
    return local_available_ports

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
    start_time = time.time()
    available_ports = []
    try:
        with ProcessPoolExecutor(max_workers=8) as executor:
            # Split the port range into chunks for parallel processing
            chunk_size = 1000
            futures = []
            for start_port in range(0, 65536, chunk_size):
                end_port = min(start_port + chunk_size - 1, 65535)
                futures.append(executor.submit(init, ip_address, start_port, end_port))
            
            # Wait for all futures to complete
            for future in futures:
                available_ports.extend(future.result())
    except KeyboardInterrupt:
        executor.shutdown(cancel_futures=True)
    print(f"Available ports on {ip_address}: {available_ports}")
    print("Script finished running.")
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
