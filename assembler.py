"""Basic assembler

This is a basic assembler, written as an educational exercise in parsing files and writing regular expressions in python.
"""

import os
from textx.metamodel import metamodel_from_file

def _parse_asm(line):
    """Converts a singe line of assembly code into a 32-bit binary instruction
    """
    return bin

class Assembler:
    """Assembler for custom assembly code
    """


    def __init__(self):
        # Generate metamodel from specification file
        self.mm = metamodel_from_file('basic_assembly.tx')
        
        # Register object processors to validate/convert data types
        self.mm.register_obj_processors({
            'int': self.handle_int # Ensure int is a positive integer
        })

    def compile(self, filename):
        # Split fname into name and extension
        asmname, _ = os.path.splitext(filename)

        self.model = self.mm.model_from_file(asmname + '.asm')

    def handle_int(self, integer):
        """Convert hexidecimal and binary numbers in strings to integers, if needed, and assert non-negativity 
        """
        if isinstance(integer, int):
            val = integer
        else:
            val = int(integer, 0)
        
        assert val>=0, "Negative integers not supported"
        return val
        

# def assemble(fname):
#     """Generates a binary file for a supplied assembly file

#     The assembler makes two passes through the .asm file. The first pass is to check syntax, convert non-jump assembly instructions into machine code, and record the location of labels. The second pass generates the jump instructions.

#     fname can be supplied with or without extension (e.g. example or example.asm), but the actual file must be named example.asm
#     """
#     # Split fname into name and extension
#     asmname, _ = os.path.splitext(fname)

#     # Generate textX metamodel
#     mm = metamodel_from_file()


#     try:
#         # Generate machine code file 
#         f_o = open(asmname + '.o', 'wb')

#     finally:
#         # Close files
#         f_o.close()
