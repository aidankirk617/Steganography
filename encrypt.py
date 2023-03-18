##############################################################
# Project 4 CS 352 : Functional Programming
# Date: 5/07/21
# Authors: Aidan Kirk, Melanney Orta
# Description:
#
# This file uses the Pillow Image library to encrypt a message
# that the user inputs into an image that can later be decrypted.
##############################################################


def ascii_con(message):  # Pure function
    """This function converts data into binary.

    This function takes a given message and converts it into binary form to be
    used later when it is encrypted into an image.

    Args:
        message: The data that will be converted to binary
    Returns:
         convert: The converted data
    """

    def formatting(char):
        """Changes a character into its binary form.

        This function takes its given character and converts it into binary

        Args:
            char: The character to convert
        Returns:
            The converted character
        """
        return format(ord(char), '08b')

    convert = map(formatting, message)  # map() higher order function
    return list(convert)


def png_change(jpg, message):
    """This function modifies the image

    This function modifies the data of the given image to change the pixels of
    the image in order to hide the message within.
    Args:
        jpg: The data of the image
        message: The message to be encrypted into the image
    """
    convert = ascii_con(message)
    jpg_iter = iter(jpg)

    for i in range(len(convert)):

        bit_len = 8
        section = jpg_iter.__next__()[:3]
        iterate = (lambda sec: sec + sec + sec)(section)  # Lambda

        jpg = [val for val in iterate]  # List comprehension

        for j in range(bit_len):
            if convert[i][j] == '0':
                if jpg[j] % 2 != 0:
                    jpg[j] -= 1

            elif convert[i][j] == '1':
                if jpg[j] % 2 == 0:
                    if jpg[j] != 0:
                        jpg[j] -= 1
                    else:
                        jpg[j] += 1

        if i == len(convert) - 1:
            if jpg[-1] % 2 == 0 and jpg[-1] != 0:
                jpg[-1] -= 1
            else:
                jpg[-1] += 1

        else:
            if jpg[-1] % 2 != 0:
                jpg[-1] -= 1

        jpg = tuple(jpg)
        yield jpg[0:3]
        yield jpg[3:6]
        yield jpg[6:9]


def encrypt_jpg(new_image, message):
    """This function puts pixels in the image.

    This function actually puts the modified pixels from png_change into the
    image to encode the message using a nested function.

    Args:
        new_image: The copy of the original image that will have the message
        message: The message to be encrypted into the image
    Returns:
        nested_encrypt: A function that will be called later
    """
    width = new_image.size[0]
    (x, y) = (0, 0)

    def nested_encrypt():  # Closure
        """This function does the work of putting pixels into the image

        This function does the actual work of putting modified pixels that
        will encrypt the message into the image
        """
        nonlocal x, y
        for jpg in png_change(new_image.getdata(), message):

            new_image.putpixel((x, y), jpg)
            if x == width - 1:
                x = 0
                y += 1
            else:
                x += 1

    return nested_encrypt  # Return a function definition


def encrypter(img_file, image_opener, message):
    """This function calls other functions to encrypt the image

    This function calls the other functions in this file to actually encrypt
    the image with the message provided (or modified by user). It will throw an
    error if the message given is empty.

    Args:
        img_file: the file to encrypt
        image_opener: the function that opens image files
        message: the message to encrypt in the image
    """

    image = image_opener(img_file)

    if len(message) == 0:
        raise ValueError('Message is empty')

    new_image = image.copy()
    enc = encrypt_jpg(new_image, message)
    enc()

    # This var below can be edited to change the name of the encrypted file
    new_image_name = "secret.png"
    new_image.save(new_image_name, str(new_image_name.split(".")[1].upper()))
    print("Done")
