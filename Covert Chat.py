# Import necessary modules
import socket
from binascii import unhexlify
from time import time
import sys

# Time constants for covert message
ZERO = 0.025
ONE = 0.1

# Socket setup: IP and port can change
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "138.47.102.201"  # Server IP address
port = 33333  # Server port number

# Connect to the server
s.connect((ip, port))

# Fill a data buffer with 4096 bytes
data = s.recv(4096)

# Create a string to store the covert binary message
covert_bin = ""

# Receive and process the entire covert message
while (data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)  # Print the received data to stdout
    sys.stdout.flush()

    # Measure the time delay (delta) between receiving data
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    delta = round(t1 - t0, 3)

    # Logic for unveiling the covert message
    if delta >= ONE:
        covert_bin += "1"
    else:
        covert_bin += "0"

s.close()  # Close the connection to the server

covert = ""
i = 0
# Process the covert binary string into ASCII
while i < len(covert_bin):
    # Process one byte (8 bits) at a time
    b = covert_bin[i:i + 8]

    # Convert the binary string to an ASCII integer
    n = int("0b{}".format(b), 2)

    try:
        covert += unhexlify("{0:x}".format(n))  # Convert to ASCII character
    except TypeError:
        covert += "?"  # Handle exceptions with a '?' character

    i += 8  # Move to the next byte in the covert binary string

# Print the covert message (excluding the last 4 characters, which are "EOF")
print(covert[0:-4])