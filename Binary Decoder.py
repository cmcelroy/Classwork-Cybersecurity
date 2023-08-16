
from sys import stdin

#decodes binary to char.
def decode(binary):
    byte = int(binary,2)

    #checks for backspace
    if(byte == 8):
        return -1
    char = chr(byte)

    return char

def bit_7(binStr):
    #splits the binary string a sequence of 7
    binArr = [binStr[i:i+7] for i in range(0, len(binStr), 7)]

    charStr = ""
    
    #converts binary strings to a characters and appends
    for i in range(0, int(len(binStr) / 7)):
        charChck = decode(binArr[i])

        if(charChck != -1):
            charStr += charChck
        else:
            charStr = charStr[:-1]

    return charStr
    
def bit_8(binStr):
    #splits the binary string a sequence of 7
    binArr = [binStr[i:i+8] for i in range(0, len(binStr), 8)]

    charStr = ""
    
    #converts binary strings to a characters and appends
    for i in range(0, int(len(binStr) / 8)): 
        charCheck = binaryToChar(binArr[i])

        if(charChck != -1):
            charStr += charChck
        else:
            charStr = charStr[:-1]

    return charStr

def main():
    binary = stdin.read().rstrip("\n")

    #7 bit Binary
    if (len(binary) % 7 == 0):
        print(bit_7(binary))
    
    #8 bit Binary
    if (len(binary) % 8 == 0):
        print(bit_8(binary))

main()