"""This script scans the ports of the local machine and prints out the open ports. """
from scapy.all import IP, TCP, sr1 # TODO: Something is wrong with this import
import socket

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def scan_port(target, port):
    # Create a SYN packet
    packet = IP(dst=target) / TCP(dport=port, flags="S")

    # Send the packet and wait for a response
    response = sr1(packet, timeout=1, verbose=0)

    # Check if the response has a SYN-ACK flag set
    if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
        print(f"Port {port} on {target} is open! ⚠️")
    else:
        print(f"Port {port} on {target} is closed.")

def scan_ports(target, start_port, end_port):
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

if __name__ == "__main__":
    # Get the local machine's IP address
    target_ip = get_local_ip()

    print(f"Scanning ports for {target_ip}")

    # Define the range of ports to scan
    start_port = 1
    end_port = 1024  # Adjust the range of ports based on your needs

    # Perform the scan
    scan_ports(target_ip, start_port, end_port)
