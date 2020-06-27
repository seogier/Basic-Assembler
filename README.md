# Basic-Assembler
Basic assembler written in Python.

This is a basic assembler for a very basic Domain Specific Language (DSL).

This DSL, which we call Basic Assembly, is a minimal assembly language for a hypothetical minimal Instruction Set Architecture (ISA)

## Implementation
The Basic Assembler is implemented in Python 3, using the [textX module](https://github.com/textX/textX) for parsing.

## Instruction Set Architecture


### Instruction Format
| Opcode  | Arg 1  | Arg 2  |
|---------|--------|--------|
| 16 bits | 8 bits | 8 bits |

16-bit opcodes are not necessary, but they make the command fit nicely into a 32-bit word.

### Instruction Set
| Command      | Mnemonic | Opcode |
|--------------|----------|--------|
| Add          | add      | 0b00   |
| Subtract     | sub      | 0b01   |
| Jump         | jmp      | 0b10   |
| No Operation | nop      | 0b11   |

The remaining 14 bits of the opcode are filled with zeros.