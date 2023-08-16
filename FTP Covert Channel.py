# Import necessary module for FTP operations
import ftplib

# Set FTP server details
ftp_addr = 'jeangourd.com'  # FTP server address
ftp_user = 'anonymous'  # FTP username (anonymous)
ftp_dir = "10"  # FTP directory
METHOD = 10  # Covert extraction method

# Function to decode binary message into a string
def decode(message):
    output = ""
    for binary in message:
        output += chr(int(binary, 2))  # Convert binary to ASCII and append to output
    return output

# Function to extract covert message from file listing permissions
def getCovert(listing):
    permissions = ""
    for item in listing:
        permissions += item[:10]  # Extract the first 10 characters from each item (permissions)
    binary = ""
    for bit in permissions:
        if (bit == '-'):
            binary += '0'  # Convert '-' to binary '0'
        else:
            binary += '1'  # Convert any other character to binary '1'

    # Extract covert message based on the specified method
    if (METHOD == 7):
        chunks = []
        i = 0
        while (i < len(binary)):
            chunks.append(binary[i:i+10])  # Divide binary string into chunks of 10 bits
            i += 10
        newbinary = []
        for chunk in chunks:
            if (chunk[0] != '1' and chunk[1] != '1' and chunk[2] != '1'):
                newbinary.append(chunk)  # Append chunks that don't start with '111'

    elif (METHOD == 10):
        if (len(binary) % 7 != 0):
            for i in range(0, len(binary) % 7):
                binary += '0'  # Ensure binary length is divisible by 7
        newbinary = []
        i = 0
        while (i < len(binary)):
            newbinary.append(binary[i:i+7])  # Divide binary string into chunks of 7 bits
            i += 7

    return newbinary  # Return the extracted covert message in binary form

# Function to perform FTP operations and extract covert message
def ftp():
    s = ""
    ftp = ftplib.FTP(ftp_addr)  # Create an FTP object
    ftp.login(user=ftp_user)  # Log in to the FTP server
    if (ftp_dir != ""):
        ftp.cwd(ftp_dir)  # Change to the specified directory within the FTP server
    listing = []
    ftp.dir(listing.append)  # List files and directories and append to the 'listing' list
    m = getCovert(listing)  # Extract covert message from listing

    s = decode(m)  # Decode the covert binary message into a string
    return s

# Main entry point of the program
if __name__ == "__main__":
    s = ftp()  # Call the 'ftp' function to extract the covert message
    print(s)  # Print the extracted covert message