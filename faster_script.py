import socket
import sys
import time
from concurrent.futures import ProcessPoolExecutor


available_ports = []

def init(ip_address, start_port, end_port):
    print(f"Initializing connection to {ip_address}")
    for i in range(start_port, end_port + 1):
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
        ip_address = sys.argv[1]
    else:
        print("No IP address provided. Please provide an IP address as a command line argument.")
        print("Example: python script.py 0000.000.000.000")
        sys.exit(1)
    print("Starting the script...")
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        # Split the port range into chunks for parallel processing
        chunk_size = 1000
        futures = []
        for start_port in range(0, 65536, chunk_size):
            end_port = min(start_port + chunk_size - 1, 65535)
            futures.append(executor.submit(init, ip_address, start_port, end_port))
        
        # Wait for all futures to complete
        for future in futures:
            future.result()
    print(f"Available ports on {ip_address}: {available_ports}")
    print("Script finished running.")
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
