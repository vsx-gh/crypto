# crypto
Python implementations of popular cryptography algorithms  
Jeff VanSickle  
Fall 2016  
---

This project is my attempt to build Python implementations of popular and/or
common approaches in cryptology. These were inspired by my reading of *The Code
Book* in late 2015. 

**Disclaimer**: This code is my own. I am responsible for any
horrendous inefficiencies or mistakes. As these programs were among my first
attempts at Python, there are most likely (definitely!) places where things
could be cleaned up. Another day, perhaps.

I come back to this repo once in a while, but I haven't had much time in the
past year. As such, I only have the Caesar cipher completed. The next item here
will be a shot at the Vigenere cipher.

Basic setup is intended as follows:
1) Import crypto.py into your program
2) Make use of the classes/functions in crypto.py to build something

I played with Tkinter a bit to make a GUI version of the Caesar.py program. It
runs great on OS X, where I built it using py2app. YMMV. If porting to another
OS, you'll likely need to change which Tkinter modules you import. I understand
that it's often just a matter of which letters are capitalized, though it can
be a bear understanding which ones. Best of luck.


### LICENSES

Code in this repo is covered by an MIT license. Please see LICENSE.txt for info.
