#!/usr/bin/env python3

'''
Program:      vigenere.py
Author:       Jeff VanSickle
Created:      20171031

Program models a Vigenere cipher. Asks for input from the user,
then encrypts the message using Vigenere's algorithm. User can
specify a keyword to use in the key.

This version does a 1:1 transfer of non-alphabetic characters
(excluding spaces, which are trimmed out). This does not aid
the encryption and in fact probably weakens it, since it is 
easier to detect patterns. This is entirely moot, as the Vigenere
cipher is not "le chiffre indechiffrable" as it was once considered.
Just have fun.

INSTRUCTIONS:
'''

import argparse
import string
import getpass
import crypto

# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--inputtext',
                    required=True,
                    type=str,
                    help='Text to encrypt/decrypt'
                    )
parser.add_argument('-o', '--operation',
                    required=True,
                    type=str,
                    choices=['encrypt', 'decrypt'],
                    help='Operation to perform'
                    )
all_args = parser.parse_args()
str_in = all_args.inputtext.upper().replace(' ', '')
vig_op = all_args.operation

# Enter key without specifying as argument
cryptkey = getpass.getpass('Key word/phrase: ').upper().replace(' ', '')

if __name__ == "__main__":
    alph_arr = crypto.build_vig_table()

    textlen = len(str_in)
    keylen = len(cryptkey)

    keyphrase = (cryptkey * int(textlen / keylen) 
                + cryptkey[0:textlen % keylen]).upper()

    if vig_op == 'encrypt':
        output = crypto.vig_encrypt(alph_arr, keyphrase, str_in)
    else:
        output = crypto.vig_decrypt(alph_arr, keyphrase, str_in)

    print(output)
