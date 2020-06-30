# Basic-Assembler
This is an assembler written in Python for a very basic Domain Specific Language (DSL).

This DSL, which we call Basic Assembly, is a minimal assembly language for a hypothetical minimal Instruction Set Architecture (ISA)

## Implementation
The Basic Assembler is implemented in Python 3, using the [textX](https://github.com/textX/textX) module for parsing.

## Basic Assembly Language

The basic assembly language was inspired by x86 and ARM assembly. It _does not_ use any form of line ending symbol (no `;`), and generally ignores extra whitespace.

### Number Representation

Only integers are supported, which can be specified in three ways: decimal (`12`), hexidecimal (`0xC`), or binary (`0b1100`).

### Labels

A Label consists of a string of numbers and characters followed by a `:`.

```
Example_label:
    add 1, 1
```

### Operations

Operations are in the format `mnemonic (arg1) (arg2)` and are typically written one-per-line.

#### No Operation

The no operation command is simply `nop`

The following is an example of a do-nothing loop:

```
loop_start:
    nop
    jmp loop_start
```

#### Arithmetic

The arithmetic operations are generic addition and subtraction operators - they do not specify what is done with the result.

| Operation | Mnemonic | Arg 1    | Arg 2      |
|-----------|----------|----------|------------|
| Add       | add      | Addend 1 | Addend 2   |
| Subtract  | sub      | Minuend  | Subtrahend |

Example:

```
    add 1, 0x01
    sub 0b1010, 2
```

#### Jump

The jump command is `jmp` followed by the label to jump to.

Example of an infinite loop:

```
Start:
    // Do somehting we wish to repeat
    jmp Start
```

### Comments

Only `//`-style comments are supported.

```
// This is a comment
```

## Instruction Set Architecture
The ISA is big-endian.

### Instruction Format
Arithmetic operations with two arguments:

| Opcode  | Arg 1  | Arg 2  |
|---------|--------|--------|
| 16 bits | 8 bits | 8 bits |

Jump Instructions:

| Opcode  | Destination   |
|---------|---------------|
| 16 bits | 16 bits       |

Nop instruction:

| Opcode  | Zeros   |
|---------|---------------|
| 16 bits | 16 bits       |

16-bit opcodes are not necessary, but they make the full instruction fit nicely into a 32-bit word.

### Instruction Set
| Command      | Mnemonic | Opcode |
|--------------|----------|--------|
| Add          | add      | 0b00   |
| Subtract     | sub      | 0b01   |
| Jump         | jmp      | 0b10   |
| No Operation | nop      | 0b11   |

The remaining 14 bits of the opcode are filled with zeros.