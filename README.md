# SecretMessageMaker
A simple program used to introduce kids to programming. Turns a human readable string into a non-human readable string in a deterministic way. Used to introduce kids to simple constructs like if-then statements and how letters and numerically represented in computers.

## Dependencies
On Linux, you will first need to install python:
```
$ sudo apt-get install python-dev
```
This is built and tested for **Python Version: X.XX**

## Usage
```
[TODO]]
```

## Overview
### Input
A short, human-readable text file. No UNICODE characters are supported.

### Output
A bloated, garbled version of the input text. This is created simply by inserting random letters in between valid letters, and shifting valid letters by a constant amount.

### Example Usage
**Input**
```
Hello, my name is Timmy and I am in 5th grade.
```

Running the SecretMessageMaker on this input file in encryption-mode would result in:
```
[TODO]
```

This pseudo-encrypted file can then be turned back into readable text by running SecretMessageMaker in decrypt mode:
```
Hello, my name is Timme and I am in 5th grade.
```
