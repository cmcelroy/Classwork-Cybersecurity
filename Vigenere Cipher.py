
import sys
import argparse
import enum
import string



#encrypt
def encrypt(plaintxt, key):
    plain = list(plaintxt)
    key = list(key)
    cipher = [] * len(plaintxt)
    tracker = 0
    
    #cycle through plain text
    for i in range(0, len(plain)):
    
        if (tracker == len(key)):
            tracker = 0
            
        #verify letter of the plain text is an alphabet character and adds int value
        if (plain[i].isalpha()):
            plainInt = asciiVal(plain[i])
            keyInt = asciiVal(key[tracker])
            cipherInt = (plainInt + keyInt) % 26
            tracker += 1
            
        #add symbol or numerical value
        else:
            cipherInt = plain[i]

        cipher.append(cipherInt)

    return cipher
    
#decrypt
def decrypt(ciphertxt, key):
    cipher = list(ciphertxt)
    key = list(key)
    plain = [] * len(ciphertxt)
    tracker = 0
    #cycle through plain text
    for i in range(0, len(cipher)):
        
        if (tracker == len(key)):
            tracker = 0
            
        #verify letter of the cipher text is an alphabet character and adds int value    
        if (cipher[i].isalpha()):
            cipherInt = asciiVal(cipher[i])
            keyInt = asciiVal(key[tracker])
            plainInt = (cipherInt - keyInt + 26) % 26
            tracker += 1
            
        #add symbol or plaintxtList to list
        else:
            plainInt = cipher[i]

        plain.append(plainInt)

    return plain

# returns the letter value of a number
def charVal(int, case):

    #get lowercase alphabet
    if case == True:
        alph = list(string.ascii_lowercase)
        
    #if uppercase
    else:
        alph = list(string.ascii_uppercase)
        
    #return letter
    return alph[int]

# returns the number value of a letter
def asciiVal(letter):

    #get lowercase alphabet
    if letter.islower():
        alph = list(string.ascii_lowercase)
        
    #get uppercase alphabet
    else:
        alph = list(string.ascii_uppercase)
    
    #return letter in alphabet
    for i in range(len(alph)):
        if (alph[i] == letter):
            return i
        



# MAIN CODE #
def main():
    
    #implement argparse for help/error indication
    parser = argparse.ArgumentParser(prog='Vigenere', description='Encrypts / Decryptsan input using a Vigenere Cipher')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt', help='Encrypts a string by using a given key.')
    group.add_argument('-d', '--decrypt', help='Decrypts a string by using a given key.')
   
    
    args = parser.parse_args()
    
    #remove spaces from key
    key = sys.argv[2]
    key = key.replace(" ", "")

    #encrypt
    if (sys.argv[1] == "-e"):
    
        while(True):
            try:
                ciphertxt = ""
                plaintxt = input()
                plaintxtList = list(plaintxt)
            
                #encrypt plaintxt to int
                intList = encrypt(plaintxt, key)
            
            
                #convert int to letter
                for i in range(0, len(intList)):
            
                    #if object = int, convert to letter
                    if(isinstance(intList[i], int)):
                        ciphertxt += str(charVal(intList[i], plaintxtList[i].islower()))
                
                    #add symbol or numerical value
                    else: 
                        ciphertxt += intList[i]

                print(ciphertxt)
            #allow for keyboard interrupt
            except KeyboardInterrupt:
                sys.exit(1)

            #handle EOF errors    
            except EOFError:
                sys.exit(1)

      
    #decrypt     
    elif (sys.argv[1] == "-d"):
        while(True):
            try:
                plaintxt = ""
                ciphertxt = input()
                plaintxtList = list(ciphertxt)
            
                #decrypt ciphertxt to int
                intList = decrypt(ciphertxt, key)
            
                ##convert int to letter
                for i in range(0, len(intList)):
            
                    #if object = int, convert to letter
                    if(isinstance(intList[i], int)):
                        plaintxt += str(charVal(intList[i], plaintxtList[i].islower()))
                
                    #add symbol or numerical value
                    else:
                        plaintxt += intList[i]
                
                print(plaintxt) 
            
            #allow for keyboard interrupt
           #allow for keyboard interrupt
            except KeyboardInterrupt:
                sys.exit(1)

            #handle EOF errors    
            except EOFError:
                sys.exit(1)
main()