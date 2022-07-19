#! /usr/bin/python3

# Import some modules we need
from random import sample
from string import ascii_letters, digits, punctuation

# Call the script with the length of password you want
from sys import argv

# Combine ALL the characters
rchar = ascii_letters + digits + punctuation

# argv needs to be an integer for sample()
pwdlen = int(argv[1])

# Prints out your new freshly randomized password =)
print("".join(sample(rchar,pwdlen))) 
