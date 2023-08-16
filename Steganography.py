
import sys
import binascii

# declare arg variables
ENCODE = "unset"
BIT = "unset"
OFFSET = 1024
INTERVAL = 1
WRAPPER = "unset"
HIDDEN = "unset"
ENDIAN = False

arguments = sys.argv[1:]
for args in arguments:
    # format
	if "-help" in args[0:2]:
			sys.stdout.write("Format: python steg.py -(s/r) -(b/B) -o<val> -i<val> -w[file] -h[file] > [outfile]\n")
			sys.exit()
    # store
	if "-s" in args[0:2]:
		ENCODE = True
	# retrieve
	if "-r" in args[0:2]:
		ENCODE = False
	# bit
	if "-b" in args[0:2]:
		BIT = True
	# byte
	if "-B" in args[0:2]:
		BIT = False
    # edian
	if "-e" in args[0:2]:
		ENDIAN = True
    # offset
	if "-o" in args[0:2]:
		OFFSET = int(args[2:] )	 
	# interval
	if "-i" in args[0:2]:
		INTERVAL = int(args[2:])
    # wrapper
	if "-w" in args[0:2]:
		WRAPPER = args[2:]
	# hidden
	if "-h" in args[0:2]:
		HIDDEN = args[2:]

# Sentinel Bytes
sentiBytes = [chr(0x0),chr(0xFF),chr(0x0),chr(0x0),chr(0xFF),chr(0x0)]
# Sentinel Binary(format)
sentiBin = ["00000000", "11111111", "00000000", "00000000", "11111111", "00000000"]
# wrapper error
if (WRAPPER == "unset"):
	sys.stdout.write("Improper format: -help to show poper format.")
	sys.exit("A wrapper file is required (-w[file])")
# encode/decode error
if (ENCODE == "unset"):
	sys.stdout.write("Improper format: -help to show poper format.")
	sys.exit("User must choose -(s/r) (store/retrieve")

# convert file to binary
def fileToBin(fileName):
	binaryArray = []
	fileIn = open(fileName, "rb")
	contents = fileIn.read()
	fileIn.close
    # create a binary array
	binaryArray = bytearray(contents)
		
	return binaryArray

# recieves array, and produces new output
def output(outputArr):
	for byte in outputArr:
		sys.stdout.write(byte)
		
	
# for encoding
if(ENCODE):
	
	# get binary array from the file to hide
	hiddenBin2 = fileToBin(HIDDEN)
	# append the sentinel to the binary array
	for item in sentiBin:
			hiddenBin2.append(item)

	storeBin = fileToBin(WRAPPER)
	

	# traverse list of hidden values
	j = 0
	for i in range(len(hiddenBin)):
		if (BIT):
			#Use a for loop, loops through the entire byte of hidden data
			for k in range(0,8):

				# set value at offset, AND 11111110, and convert to binary, convert to string
				storeBin[OFFSET] = str(bin(int(storeBin[OFFSET],2) & int("11111110",2))[2:].zfill(8))

				# AND the value inside of hidden list, get the smallest bit, OR the value with storage.
				storeBin[OFFSET] = str(bin(int(storeBin[OFFSET],2) | ((int(hiddenBin[j],2) & int("10000000")) >> 7))[2:].zfill(8))

				# change value of hidden list to shift to the right, continue in for loop
				hiddenBin[j] = str(bin(int(hiddenBin[j],2) << 1)[2:].zfill(8))

				# offset increases, to navigate to next interval
				OFFSET+=1
			#increase j, to continue to traverse down the list of hidden values
			j+=1
			
		else:
			#replace the entire byte in array with byte in hidden list
			storeBin[OFFSET] = hiddenBin[i]

			# increase interval
			OFFSET+=INTERVAL
	
	output(storeBin)

# for decoding
else:

	storeBin = fileToBin(WRAPPER)

	newFile = []
	sentiLength = len(sentiBytes)
	
	# continue until sentinel is reached
	while sentiBytes != newFile[-sentiLength:]:
		if (BIT):
            # creates a new string that is null
			newString = ""
			for bit in range(0,8):
				if (ENDIAN):
					# get last bit, add to beginning of byte
					newString = str(1 & storeBin[OFFSET]) + newString
				else:
					# get last bit, add to end of byte
					newString += str(1 & storeBin[OFFSET])
					OFFSET+=INTERVAL

			# when bit is full, add to the newFile str
			newFile.append(chr(int(newString,2)))
			
		else:
			byte = chr(storeBin[OFFSET])
            # take byte in storage bin, and add to newFile list
			newFile.append(byte)
			OFFSET+=INTERVAL
	
	#Remove the sentinel from the end of the array
	newFile = newFile[:-7]
	# output of newFile
	output(newFile)