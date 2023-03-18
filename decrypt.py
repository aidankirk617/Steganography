##############################################################
# Project 4 CS 352 : Functional Programming
# Date: 5/07/21
# Authors: Aidan Kirk, Melanney Orta
# Description:
#
# This file uses the Pillow Image library to decrypt a message
# that is in a image file given by the user. The message is
# printed out once decrypted.
##############################################################
import math
from functools import reduce


def decrypter(img_file, image_opener):
    """This function decrypts a message from an image.

    This function uses the Pillow Image library to look through an image given
    by the user. It looks for a message that was encrypted using the encrypt
    option in this program and returns it to get printed.

    Args:
        img_file: the name of the file that is being decrypting
        image_opener: the function that opens image files
    Returns:
        text: The string containing the message that was decrypted
    """
    image = image_opener(img_file)

    message = []
    image_data_iter = iter(image.getdata())

    while True:
        jpgs = [val for val in image_data_iter.__next__()[:3] +
                image_data_iter.__next__()[:3] +
                image_data_iter.__next__()[:3]]  # List comprehension

        def not_a_num(val):
            """Filters out parameters that are not numbers

            This function returns false if the parameter not a number, which
            will be used in conjunction with the filter() function.

            Args:
                val: the parameter to check
            Returns:
                False if it is not a number, True otherwise
            """
            if math.isnan(val):
                return False
            else:
                return True

        jpgs = list(filter(not_a_num, jpgs))  # filter() higher order function

        binary = ''

        for i in jpgs[:8]:
            if i % 2 == 0:
                binary = (lambda zero: zero + "0")(binary)  # lambda
            else:
                binary = (lambda one: one + "1")(binary)  # lambda

        letter = chr(int(binary, 2))
        message.append(letter)
        if jpgs[-1] % 2 != 0:
            text = reduce(lambda a, b: a + b, message)  # reduce() and lambda
            return text
