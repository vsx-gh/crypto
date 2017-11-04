#!/usr/bin/env python3

'''
Program:      crypto.py
Author:       Jeff VanSickle
Created:      20151114 

Library of crypto functions. Includes following algorithms:
    - Caesar shift
    - Vigenere

INSTRUCTIONS:
    - Line 54 (or thereabouts): set location of your dictionary file

'''

import string

def crypt_caesar(msg_in, offset):
    ''' Encrypts or decrypts using Caesar shift cipher '''
    crypt_string = ""
    base_alphabet = string.ascii_uppercase

    # Build the shifted alphabet. Letter at offset in base_alphabet becomes new "A"
    shift_start_index = (26 - offset) % 26 
    shift_alphabet =  base_alphabet[shift_start_index:] + base_alphabet[0:shift_start_index]

    # Parse input string and convert to either base or (en|de)crypted alphabet by index match
    for letter in msg_in.upper():
        if letter not in base_alphabet:
            shift_letter = letter
        else:
            shift_letter = shift_alphabet[base_alphabet.find(letter)]
        crypt_string += shift_letter

    return crypt_string    # Give back converted string/message


def find_shift(msg_in):
    ''' Analyzes all shifts for input string. Intended to brute force input string by
        finding all possibilities. Also checks if decrypted possibilities are in the
        English dictionary.'''
 
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    crypto_start_index = 1
    candidate_index = 1
    highest_dict_matches = 0

    # Base for dictionary search. Copied from OS X /usr/share/dict/words
    dict_file = open("<YOUR_DICTIONARY_FILE>","r").read()

    # Analysis header. Spacing not ideal.
    spacer = " " * (len(msg_in) - 10)
    dasher = "-" * (len(spacer) + 24)
    print("\n\nSHIFT DECRYPTED", spacer, "IN_DICT")
    print(dasher)
 
    # Cycle through index shifts, starting at 1
    while crypto_start_index < 26:
        crypt_string = ""
        shift_alphabet =  base_alphabet[crypto_start_index:] + base_alphabet[0:crypto_start_index]
        num_dict_matches = 0

        # Convert letter-by-letter and build converted string. Preserve spaces.
        for letter in msg_in.upper():
            if letter not in base_alphabet:
                crypt_letter = letter
            else:
                crypt_letter = shift_alphabet[base_alphabet.find(letter)]

            crypt_string += crypt_letter
 
        # For each unit in message/phrase, check if in dictionary
        for word in crypt_string.split(" "):
            if word.lower() in dict_file:
                num_dict_matches = num_dict_matches + 1

        # Make current candidate the likely index if highest dictionary matches
        if num_dict_matches > highest_dict_matches:
            highest_dict_matches = num_dict_matches
            candidate_index = crypto_start_index

        # Make output spacing line up
        if crypto_start_index < 10:
            print('{} :   {}    {}'.format(crypto_start_index, crypt_string, num_dict_matches))
        else:
            print('{}:   {}    {}'.format(crypto_start_index, crypt_string, num_dict_matches))

        crypto_start_index = crypto_start_index + 1
 
    # Give us some space before returning prompt
    print("\nBest guess on correct shift: ", candidate_index, "\n\n")



def build_vig_table():
    alph_array = []
    base_alph = string.ascii_uppercase

    # Populate all alphabets
    for line_num in range(0, 26):
        # Chop off first chars, append to end of line
        table_line = base_alph[line_num:] + base_alph[0:line_num]
        alph_array.append(table_line)

    return alph_array



def vig_encrypt(alphabets, vig_key, input_text):
    encr_str = ''
    for letter in range(0, len(vig_key)):
        if input_text[letter] not in string.ascii_uppercase:
            encr_str += input_text[letter]
            continue

        row = alphabets[alphabets[0].find(vig_key[letter])]
        col = row[alphabets[0].find(input_text[letter])]
        encr_str += col 

    # Encrypted string
    return encr_str



def vig_decrypt(alphabets, vig_key, input_text):
    decr_str = ''
    for letter in range(0, len(vig_key)):
        if input_text[letter] not in string.ascii_uppercase:
            decr_str += input_text[letter]
            continue

        row = alphabets[alphabets[0].find(vig_key[letter])]
        orig_pos = row.find(input_text[letter])
        col = alphabets[0][orig_pos]
        decr_str += col

    # Decrypted string
    return decr_str
