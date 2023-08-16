
import socket
from binascii import hexlify
import time

# Define time constants for transmission
ZERO = 0.025
ONE = 1

try:
    # Create a socket object and bind it to a port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 65432
    s.bind(("", port))
    s.listen(0)
except:
    print("Connection Error")  # Print an error message if socket creation fails

# Accept incoming connection
c, addr = s.accept()

# Define the original message and covert message to be sent
msg = "This message is going to be longer so that it can pass the covert message."
covert = "secret" + "EOF"

# Convert covert message characters to binary and append to covert_bin
covert_bin = "010000010100001001000011"  # Binary representation of 'secret'
for i in covert:
    covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)  # Convert character to binary and append

n = 0
# Iterate through each character in the original message
for i in msg:
    c.send(i)  # Send the character over the connection

    if covert_bin[n] == '0':
        time.sleep(ZERO)  # If covert bit is 0, sleep for a short time
    else:
        time.sleep(ONE)  # If covert bit is 1, sleep for a longer time

    n = (n + 1) % len(covert_bin)  # Move to the next bit in the covert message

c.send("EOF")  # Send an end-of-file marker
c.close()  # Close the connection