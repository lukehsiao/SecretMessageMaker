# SecretMessageMaker
A simple program used to introduce kids to programming. Turns a human readable string into a non-human readable string in a deterministic way. Used to introduce kids to simple constructs like if-then statements and how letters and numerically represented in computers.

## Dependencies
On Linux, you will first need to install python:
```
$ sudo apt-get install python-dev
```

On Windows, install Python 2.7 from [Python.org](https://www.python.org/ftp/python/2.7.11/python-2.7.11.msi)

This is built and tested for **Python Version: 2.7.11**

## Usage
```
usage: SecretMessageMaker.py [-h] [-e] FILE

positional arguments:
  FILE           path of input text file (required)

optional arguments:
  -h, --help     show this help message and exit
  -e, --encrypt  run program in encryption mode. Default: decrypt

```

## Overview
### Input
A short, human-readable text file. No UNICODE characters are supported. ASCII only.

### Output
A bloated, garbled version of the input text. This is created simply by inserting random letters in between valid letters, and shifting valid letters by a constant amount.

### Example Usage
Given an initial input file of filename.txt, SecretMessageMaker will turn filename.txt
into secret\_filename.txt which will be non-human-readable. If decryption is run on any file
starting with 'secret\_', the decrypted message will be the human-readable version of
secret file, and the filename will have the 'secret\_' removed.

```
message.txt:
-------------
Hello, my name is Susan and I am in 1st grade.
```

Encryption:
```
$ python SecretMessageMaker.py -e message.txt
  [info] ENCRYPTING message.txt into secret_message.txt...
```

After being encrypted, a new secret\_message file will be created and contain:
```
secret_message.txt:
------------------
72 101 108 108 111 44 32 109 121 32 110 97 109 101 32 105 115 32 83 117 115 97 110 32 97 110 100 32 73 32 97 109 32 105 110 32 49 115 116 32 103 114 97 100 101 46 10
```

Decryption:
```
$ python SecretMessageMaker.py secret_message.txt
  [info] DECRYPTING secret_message.txt into message.txt...
```

## Notes
Originally, the plan was to perform a set shift in the ascii value of the characters, and insert a set
amount of random letters in between valid letters. This would result in a much more jibberish string rather
than just simply the ascii values of each letter represented in decimal. But, the 2nd grader and kindergartener
seemed more interested in turning everything into numbers, so that's what we did.
