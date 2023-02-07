#!/usr/bin/python3
"""This module define a text file reading function"""


def read_file(filename=""):
    """This Prints th content of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
