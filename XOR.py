
import fileinput
import sys

# reads key file
keyFile = open('key', 'r')
key = keyFile.read()

# reads input file
text = sys.stdin.read()

#xor function
def xor(key, text):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(key, text))

# calls function and prints the result
print(xor(key, text))
