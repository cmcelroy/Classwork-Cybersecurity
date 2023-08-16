
# Import necessary modules
from pynput.keyboard import Key, Listener
from time import time
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

# Define the function to be called when a key is pressed
def on_press(key):
    global keysPress, pressTime
    try:
        pressTime.append(time())
        keysPress.append(key)
    except AttributeError:
        print(str(key))  # Print the key if an attribute error occurs

# Define the function to be called when a key is released
def on_release(key):
    global keysRelease, releaseTime
    releaseTime.append(time())
    keysRelease.append(key)
    if key == Key.esc:  # If the 'esc' key is pressed, stop the listener
        return False

# Initialize lists to store key press and release information
keysPress = []
pressTime = []
keysRelease = []
releaseTime = []

# Set up a listener for keyboard events using the defined functions
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Initialize an empty string to store key press and release data
string = ""

# Remove the last key press and release events (presumably the 'esc' key)
keysPress = keysPress[:-1]
keysRelease = keysRelease[:-1]

# Generate a string representation of the sequence of keys pressed
for keys in keysPress:
    string += str(keys)[2] + ","

# Generate a string representation of key pairs pressed in sequence
for i in range(len(keysPress) - 1):
    string += str(keysPress[i])[2] + str(keysPress[i + 1])[2] + ","

string = string[:-1] + "\n"  # Remove the last comma and add a newline

i = 0
# Generate timing information for key presses and releases
while True:
    if keysPress[i] == keysRelease[i]:
        string += str(releaseTime[i] - pressTime[i]) + ","
    else:
        for j in range(len(keysPress) - 1):
            if keysPress[i] == keysRelease[j] and j > i:
                string += str(releaseTime[j] - pressTime[i]) + ","
    i += 1
    if i == len(keysPress):
        break

# Generate timing information for inter-key press intervals
for i in range(len(keysPress) - 2):
    string += str(pressTime[i + 1] - pressTime[i]) + ","

string = string[:-1]  # Remove the last comma

# Print the generated data string
print(string)

# Flush the standard output buffer to ensure the printed data is displayed
tcflush(stdout, TCIFLUSH)