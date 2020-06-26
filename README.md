# Basic-Assembler
Basic Assembler written in Python.

## Instruction Format
| Opcode  | Arg 1  | Arg 2  |
|---------|--------|--------|
| 16 bits | 8 bits | 8 bits |

16-bit opcodes are not necessary, but they make the command fit into a 32-bit word

## Instruction Set
| Command      | Mnemonic | Opcode |
|--------------|----------|--------|
| Add          | add      | 0b00   |
| Subtract     | sub      | 0b01   |
| Jump         | jmp      | 0b10   |
| No Operation | nop      | 0b11   |

The remaining 14 bits of the opcode are filled with zeros