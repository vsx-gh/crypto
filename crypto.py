#!/usr/bin/env python

'''
Program:      crypto.py
Author:       Jeff VanSickle
Created:      20151114 
Modified:     20151119

Library of crypto functions. Includes Caesar shift cipher, Vigenere cipher, etc.

UPDATES:
     20151119 JV - cryptCaesar: return string instead of printing it

INSTRUCTIONS:
    - Line 54 (or thereabouts): set location of your dictionary file

'''

def cryptCaesar(msgIn, offset, cryptDirection):
    ''' Encrypts or decrypts using Caesar shift cipher '''
    cryptString = ""
    baseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Build the shifted alphabet. Letter at offset in baseAlphabet becomes new "A"
    cryptoStartIndex = (26 - offset) % 26 
    cryptoAlphabet =  baseAlphabet[cryptoStartIndex:] + baseAlphabet[0:cryptoStartIndex]

    # Parse input string and convert to either base or (en|de)crypted alphabet by index match
    for letter in msgIn:
        if letter == " ":
            cryptLetter = " "
        else:
            if cryptDirection == "D":
                index = cryptoAlphabet.find(letter, 0, len(cryptoAlphabet))
                cryptLetter = baseAlphabet[index]
            elif cryptDirection == "E":
                index = baseAlphabet.find(letter, 0, len(baseAlphabet))
                cryptLetter = cryptoAlphabet[index]
        cryptString = cryptString + cryptLetter

    return cryptString     # Give back converted string/message


def enumShift(msgIn):
    ''' Analyzes all shifts for input string. Intended to brute force input string by
        finding all possibilities. Also checks if decrypted possibilities are in the
        English dictionary.'''
    
    baseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cryptoStartIndex = 1
    candidateIndex = 1
    highestDictMatches = 0

    # Base for dictionary search. Copied from OS X /usr/share/dict/words
    dictionary = file("<YOUR_DICTIONARY_FILE>","r").read()

    # Analysis header. Spacing not ideal.
    spacer = " " * (len(msgIn) - 10)
    dasher = "-" * (len(spacer) + 24)
    print "\n\nSHIFT DECRYPTED", spacer, "IN_DICT"
    print dasher
    
    # Cycle through index shifts, starting at 1
    while cryptoStartIndex < 26:
        cryptString = ""
        cryptoAlphabet =  baseAlphabet[cryptoStartIndex:] + baseAlphabet[0:cryptoStartIndex]
        numDictMatches = 0

        # Convert letter-by-letter and build converted string. Preserve spaces.
        for letter in msgIn:
            if letter == " ":
                cryptLetter = " "
            else:
                index = baseAlphabet.find(letter, 0, len(baseAlphabet))
                cryptLetter = cryptoAlphabet[index]

            cryptString = cryptString + cryptLetter
        
        # For each unit in message/phrase, check if in dictionary
        for word in cryptString.split(" "):
            if word.lower() in dictionary:
                numDictMatches = numDictMatches + 1

        # Make current candidate the likely index if highest dictionary matches
        if numDictMatches > highestDictMatches:
            highestDictMatches = numDictMatches
            candidateIndex = cryptoStartIndex

        # Make output spacing line up
        if cryptoStartIndex < 10:
            print cryptoStartIndex, ":  ", cryptString, " ", numDictMatches
        else:
            print cryptoStartIndex, ": ", cryptString, " ", numDictMatches

        cryptoStartIndex = cryptoStartIndex + 1
    
    # Give us some space before returning prompt
    print "\nBest guess on correct shift: ", candidateIndex, "\n\n"
