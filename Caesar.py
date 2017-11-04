#!/usr/bin/env python3

'''
Program:      Caesar.py
Author:       Jeff VanSickle
Created:      20151114 

Program decrypts text encrypted with Caesar shift cipher. Asks
user for input - the encrypted text - then determines the shift
offset and performs decryption.

Program can also ENcrypt a message from user input and the
user-specified shift offset.

Program makes use of crypto.py library.

INSTRUCTIONS:

'''

import crypto

if __name__ == "__main__":
    # Get input string
    input_msg = input("Please enter your message: ")
    do_brute_force = input("Want to brute force (Y/N)? ")

    if do_brute_force == "Y":
        crypto.find_shift(input_msg)
    elif do_brute_force == "N":
        shift = input("Shift (1-25)? ")
        output_str = crypto.crypt_caesar(input_msg, int(shift))
        print(output_str)
