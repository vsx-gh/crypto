#!/usr/bin/env python

'''
File:     Caesar_GUI.py
Author:   Jeff VanSickle
Created:  20151116
Modified: 22015111

Putting Tkinter front-end on Caesar shift cipher program.

UPDATES:
    yyyymmdd JV - Changed something, commenting here

INSTRUCTIONS:

'''

from Tkinter import *
import ttk
import crypto
import tkMessageBox

# Functions!
def buttonClick():
    ''' Action processes button click, performs (en|de)cryption '''
    cryptMsg = cryptPhraseIn.get()
    cipherShift = int(shiftNumIn.get())
    
    # Shift can't be larger than alphabet
    if cipherShift < 1 or cipherShift > 25:
        tkMessageBox.showinfo("Error", "Shift must be > 0 and < 25") 

    # Encrypting or decrypting? Convert to single-letter input for function
    cryptOperation = cryptDirection.get()
   
    if cryptOperation == "Encrypt":
        cryptDir = "E"
    elif cryptOperation == "Decrypt":
        cryptDir = "D"

    # Perform encryption or decryption
    cryptMsgConv = crypto.cryptCaesar(cryptMsg.upper(), cipherShift, cryptDir)
    
    # Display results
    outMsg = "Original message: " + cryptMsg + "\n\n" + cryptOperation + ": " + cryptMsgConv + "\n"
    tkMessageBox.showinfo("Results", outMsg)
    
    return

if __name__ == "__main__":
    # Background color for all form elements
    bgColor = "#E7E7E7"

    # Make a winder
    app = Tk()
    app.title("Caesar Shift Cipher")
    app.geometry('400x200')
    app.configure(background = bgColor)

    # Create a label frame to work with
    inputFrame = LabelFrame(app, text = "Message Parameters")
    inputFrame.configure(background = bgColor)
    inputFrame.grid(row = 0, sticky = 'W', padx = 25, pady = 25)

    # Put a label in the winder
    msgInput = StringVar()
    msgInput.set("Text to encrypt/decrypt: ")
    msgLabel = Label(inputFrame, textvariable=msgInput, justify = RIGHT, width = 0)
    msgLabel.configure(background = bgColor, highlightbackground = bgColor, highlightcolor = bgColor)
    msgLabel.grid(row = 0, column = 0)

    # Get the item to encrypt/decrypt
    cryptPhraseIn = StringVar(None)
    cryptIn = Entry(inputFrame, textvariable = cryptPhraseIn, justify = LEFT)
    cryptIn.configure(width = 25, highlightbackground = bgColor)
    cryptIn.grid(row = 0, column = 1)

    shiftLabelText = StringVar()
    shiftLabelText.set("Shift (1-25): ")
    shiftLabel = Label(inputFrame, textvariable = shiftLabelText, justify = RIGHT, width = 0)
    shiftLabel.configure(background = bgColor, highlightbackground = bgColor, highlightcolor = bgColor)
    shiftLabel.grid(row = 1, column = 0)

    # Get shift
    shiftNumIn = StringVar(None)
    shiftIn = Entry(inputFrame, textvariable = shiftNumIn, justify = LEFT)
    shiftIn.configure(width = 25, highlightbackground = bgColor)
    shiftIn.grid(row = 1, column = 1)

    # Another label frame for encrypt/decrypt radio
    cryptFrame = LabelFrame(app)
    cryptFrame.configure(background = bgColor, borderwidth = 0)
    cryptFrame.grid(row = 3, sticky = 'W', padx = 25)

    # Get crypto direction (encrypt/decrypt)
    cryptDirection =  StringVar()
    cryptDirection.set(None)
    encryptRadio = Radiobutton(cryptFrame, text = "Encrypt", value = "Encrypt", background = bgColor, variable = cryptDirection)
    encryptRadio.grid(row = 3, column = 0, padx = 65)
    decryptRadio = Radiobutton(cryptFrame, text = "Decrypt", value = "Decrypt", background = bgColor, variable = cryptDirection)
    decryptRadio.grid(row = 3, column = 1, padx = 20)

    # Howz aboot a buttON?
    goButton = Button(app, text="Go", command=buttonClick)
    goButton.configure(background = bgColor, highlightbackground = bgColor)
    goButton.grid(row = 13, column = 0, pady = 10)

    # Keep it going?
    app.mainloop()
