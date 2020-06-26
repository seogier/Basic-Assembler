"""Basic assembler

This is a basic assembler, written as an educational exercise in parsing files and writing regular expressions in python.
"""

import re
import os

def _parse_asm(line):
    """Converts a singe line of assembly code into a 32-bit binary instruction
    """
    return bin

def assemble(fname):
    """Generates a binary file for a supplied assembly file

    The assembler makes two passes through the .asm file. The first pass is to check syntax, convert non-jump assembly instructions into machine code, and record the location of labels. The second pass generates the jump instructions.

    fname can be supplied with or without extension (e.g. example or example.asm), but the actual file must be named example.asm
    """
    # Split fname into name and extension
    asmname, _ = os.path.splitext(fname)
    
    # Define Regexes
    r_label = re.compile("^\S+:") # Section Label
    r_c_line = re.compile("\s?//") # // comment
    r_c_open = re.compile("\s?/\*") # /* block comment start
    r_c_close = re.compile("\s?\*/") # */ block comment stop

    # Initialize dictionary of Labels
    labels = {}

    # Initialize flag for multi-line comment
    in_comment = False

    try:
        # Open assembly file
        f_asm = open(asmname + '.asm', 'r')
        # Generate machine code file 
        f_o = open(asmname + '.o', 'wb')

        # Begin first iteration through 
        for line in f_asm.readlines():
            # Only parse if 
            if in_comment:
                # Look for end of multi-line comment
                pass
            else:
                pass


    finally:
        # Close files
        f_asm.close()
        f_o.close()
