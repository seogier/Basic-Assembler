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

        # Define opcodes
        self.opcodes = {
            'add'   :   (0).to_bytes(2, 'big'),
            'sub'   :   (1).to_bytes(2, 'big'),
            'jmp'   :   (2).to_bytes(2, 'big'),
            'nop'   :   (3).to_bytes(2, 'big')
        }

    def compile(self, filename):
        # Split fname into name and extension
        # The assembly file must have a .asm extension
        asmname, _ = os.path.splitext(filename)

        # Parse assembly file
        self.model = self.mm.model_from_file(asmname + '.asm')

        # Initialize dictionary of labels
        # key - label name
        # value - address of the following instruction
        labels = {}

        # Initialize dictionary of jump instructions
        # key - instruction address
        # value - label to jump to
        jumps = {}

        # Initialize address counter for output file
        # address counter counts instructions (not bytes) in the output file
        address = 0

        # Initialize empty bytearray to store program
        program = bytearray()

        # Convert parsed assembly into machine code
        
        # First pass fills in all non-jump commands and builds list of labels
        for statement in self.model.statements:
            # Interpret type of statement
            name = statement.__class__.__name__
            print(name)

            # Add and Subtract
            if  (name == 'add') | (name == 'sub'):
                # Generate instruction to add to program
                program += self.opcodes[name]
                program += statement.arg1.to_bytes(1, 'big')
                program += statement.arg2.to_bytes(1, 'big')
                address += 4

            # Jump
            elif name == 'jmp':
                jumps[address] = statement.label
                
                # Insert a filler instruction, to be replaced in the second pass
                program += (0).to_bytes(4, 'big')
                address += 4

            # Nop
            elif statement == 'nop': # Nop is the statement, since it contains nothing
                program += self.opcodes['nop']
                program += (0).to_bytes(2, 'big')
                address += 4

            # Label
            elif name == 'label':
                labels[statement.label] = address
            
        # Second pass fills in jump instructions
        for jump in jumps:
            # Resolve jump destination
            address = labels[jumps[jump]]
            # Generate new instruction
            instruction = self.opcodes['jmp'] + address.to_bytes(2, 'big')
            program[jump:jump+4] = instruction

        with open(asmname + '.o', 'wb') as f_o:
            f_o.write(program)
        
    def handle_int(self, integer):
        """Convert hexidecimal and binary numbers in strings to integers, if needed, and assert non-negativity 
        """
        if isinstance(integer, int):
            val = integer
        else:
            val = int(integer, 0)
        
        assert val>=0, "Negative integers not supported"
        return val

