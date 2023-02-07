#!/usr/bin/python3
"""This module define a file writing function."""


def write_file(filename="", text=""):
    """Writes a string to the text file UTF-8
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
