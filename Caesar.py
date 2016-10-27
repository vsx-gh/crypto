#!/usr/bin/env python

'''
Program:      Caesar.py
Author:       Jeff VanSickle
Created:      20151114 
Modified:     20151114

Program decrypts text encrypted with Caesar shift cipher. Asks
user for input - the encrypted text - then determines the shift
offset and performs decryption.

Program can also ENcrypt a message from user input and the
user-specified shift offset.

Program makes use of crypto.py library.

UPDATES:
     yyyymmdd JV - Changed something, commenting here

INSTRUCTIONS:

'''

import crypto

if __name__ == "__main__":

    # Get input string
    inputMsg = raw_input("Please enter your message: ")
    doBruteForce = raw_input("Want to brute force (Y/N)? ")

    if doBruteForce == "Y":
        crypto.enumShift(inputMsg)
    elif doBruteForce == "N":
        shift = raw_input("Shift (1-25)? ")
        cryptType = raw_input("Encrypt or Decrypt (E or D)? ")
        crypto.cryptCaesar(inputMsg, int(shift), cryptType)
