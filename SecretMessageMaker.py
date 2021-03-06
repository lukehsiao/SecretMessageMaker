#! /usr/bin/env python

import sys, os, io, string
import argparse

def parse_args():
    """
    Function: parse_args
    --------------------
    Parse the commandline arguments for SecretMessageMaker
    """
    # Define what commandline arguments can be accepted
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encrypt", action="store_const", const=True,
                        help="run program in encryption mode. Default: decrypt")
    parser.add_argument('filename', metavar="FILE",
                        help="path of input text file (required)")
    args = parser.parse_args()

    # Validate the filename
    file_name = args.filename

    if not os.path.exists(file_name):
        parser.error("The file %s does not exist!" % file_name)

    # Check to make sure the user isn't going to accidentally override
    # something, or accidentally encrypt something twice.
    if "secret_" in args.filename and args.encrypt:
        # If you're encrypted an already encrypted message
        parser.error("[error] You're ENCRYPTING an encrypted file!")

    elif "secret_" not in args.filename and not args.encrypt:
        parser.error("[error] You're DECRYPTING a plain file!")

    # Let the user know which commands the program sees, and which files will
    # be made.
    if args.encrypt:
        print "[info] ENCRYPTING %s into secret_%s..." % (file_name, file_name)
    else:
        print ("[info] DECRYPTING %s into %s..." % (file_name,
            file_name.replace("secret_", '')))

    return args

def encrypt(plain_line):
    """
    Function: encrypt
    --------------------
    Turns the human-readable line of text into a non-human-readable line of
    encrypted text.
    @param plain_line   the line to be encrypted
    @return             the encrypted version of the 'line'
    """
    char_list = list(plain_line)
    encrypted_list = []
    for character in char_list:
        encrypted_list.append(str(ord(character)))

    return ' '.join(encrypted_list)

def decrypt(encrypted_line):
    """
    Function: decrypt
    --------------------
    Turns the encrypted line of text into a human-readable line of text.
    @param encrypted_line   the line to be encrypted
    @return                 the encrypted version of the 'line'
    """
    num_list = encrypted_line.split()
    decrypted_list = []
    for number in num_list:
        decrypted_list.append(chr(int(number)))

    return ''.join(decrypted_list)

# Main Function
if __name__ == "__main__":
    args = parse_args() # parse commandline arguments

    # Open input file
    in_file = open(args.filename, 'r')

    # Open output file
    if args.encrypt:
        # If encrypting, append secret_ to the front
        out_file = open("secret_" + args.filename, 'w')
    else:
        # If decrypting, remove secret_ from the filename
        out_file = open(args.filename.replace("secret_", ''), 'w')

    # Iterate over every line of the file
    for line in in_file:
        if args.encrypt:
            # Run encryption algorithm
            out_file.write(encrypt(line) + ' ') # add space between lines
        else:
            # Run decryption algorithm
            out_file.write(decrypt(line))

    # Close the files that we were using
    in_file.close()
    out_file.close()
