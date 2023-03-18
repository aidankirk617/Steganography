##############################################################
# Project 4 CS 352 : Functional Programming
# Date: 5/07/21
# Authors: Aidan Kirk, Melanney Orta
# Description:
#
# Our program incorporates steganography to hide data (string, int) within
# a png file of the users choosing (catamount.png is supplied as an example).
# Users also have the option of extracting data from previously encrypted files.
# If a different file is given other than the one stored in driver.py,
# appropriate errors are called. This file calls code from decrypt.py and
# encrypt.py to decrypt messages from images and encrypt messages into images
# (acting as a driver).
##############################################################

from PIL import Image
import encrypt
import decrypt


def printer(sentence):  # Recursion
    """This function prints out a string.

    This function prints out a given string using recursion. It prints out the
    first character of a string and then calls itself with everything but the
    first character of the string. It does this until the string is empty.

    Args:
        sentence: A string containing the text that should be printed
    Returns:
        0: Once the given sentence has been printed out
    """
    if len(sentence) == 0:
        return 0
    else:
        print(sentence[0], end="")
        printer(sentence[1:])


def image_opener(img):
    """Opens an image

    Given the name of an image file, opens it and returns it to be used later.

    Args:
        img: The name of the image file
    Returns:
        image: The opened image file
    """
    image = Image.open(img, 'r')
    return image


def main():
    """This function is the entry point into the program.

    This function is the main function which calls the code in either encrypt
    or decrypt depending on what the user chooses. It prints out the message
    if decryption was chosen.
    """
    # Recursion
    printer("Functional Programming with Steganography: \n1. Encrypt\n2. "
            "Decrypt\n3. Quit\n")
    user_input = int(input(""))

    if user_input == 1:
        # Passing function definition as parameter
        encrypt.encrypter('catamount.png', image_opener, "secret")
        # The first param above can be edited to change the source image
        # The third param above can be edited to change the encrypted message

    elif user_input == 2:
        # Passing function definition as parameter
        print("Decrypted Message:",
              decrypt.decrypter('secret.png', image_opener))
        # The first param above can be edited to change the decrypted image
    elif user_input == 3:
        quit(0)
    else:
        raise Exception("ERROR: Incorrect input")


if __name__ == '__main__':
    main()
