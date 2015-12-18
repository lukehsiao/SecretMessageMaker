#! /usr/bin/env python


# Constants used to encrypt the message
EXTRA_LETTERS = 2
SECRET_SHIFT = 5

def parse_args():
    """
    Function: parse_args
    --------------------
    Parse the table extractor arguments
    """
    # Define what commandline arguments can be accepted
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encrypt", action="store_const", const=True,
                        help="run program in encryption mode. Default: decrypt")
    parser.add_argument('filename', metavar="FILE",
                        help="path of input text file (required)")
    parser.add_argument("-o","--output", action="store",
                        help="path to store the output file. Default: print to console")
    args = parser.parse_args()

    # Set the debug flag
    if args.debug:
        print "[info] Running in DEBUG mode."

    # Validate the filename
    file_name = args.filename
    if args.output is not None and not os.path.exists(args.output):
        os.makedirs(args.output)

    if not os.path.exists(file_name):
        parser.error("The file %s does not exist!" % file_name)

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
        encrypted_list.append(ord(character))

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
        decrypted_list = chr(int(number))

    return ''.join(decrypted_list)

# Main Function
if __name__ == "__main__":
    args = parse_args() # parse commandline arguments

    # Open input file
    in_file = open(args.filename, 'r')

    # Open output file
    out_file = open(args.output, 'w')

    # Iterate over every line of the file
    for line in in_file:
        if args.encrypt:
            # Run encryption algorithm
            outfile.write(encrypt(line) + '\n')
        else:
            # Run decryption algorithm
            outfile.write(decrypt(line) + '\n')
