Project 4: Functional Programming

Date: 05/07/21

Authors: Aidan Kirk, Melanney Orta

Project Description:

This project uses the Pillow image library to encrypt messages and decrypt
messages into images. It is coded using functional programming techniques. The
program consists of three files, driver.py, encrypt.py and decrypt.py.

The driver file allows the user to choose if they are encrypting a file with a
message or if they are decrypting a file with a message already in it. The
image files that are used are hard coded into the program, but can be edited
in the appropriate spots that are commented if the user desires. Users should
only use images that are in PNG format and any messages they would like to
encrypt should not include numbers (ex: 0-9).

Encrypt.py and decrypt.py have the code for their respective operations and
that code is called from the driver depending on which operation is chosen.
Within encrypt.py, the user may edit the program to change the name of the
file that is saved with the encrypted message. Users should make sure if they
edit the name that the name they choose ends with ".png" to ensure the image
file gets saved correctly.

How to run:
First, be sure to install the Pillow image library using pip by typing the
command:
    python3 -m pip install --upgrade Pillow

From there, you can run the program by typing the command:
    python3 driver.py

Known bugs:
None