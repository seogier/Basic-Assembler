"""Basic assembler

This is a basic assembler, written as an educational exercise in parsing files and writing regular expressions in python.
"""

import os
import textX

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
    
    try:
        # Open assembly file
        f_asm = open(asmname + '.asm', 'r')
        # Generate machine code file 
        f_o = open(asmname + '.o', 'wb')

    finally:
        # Close files
        f_asm.close()
        f_o.close()
