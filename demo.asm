//This is a demonstration of the features of the very basic assembbly language that has been developed for this assembler

// Let's start with a label
Label1:
    // And now some proper assembly code
    nop
    add 1, 1
    sub 2, 1
    sub 0xFF, 0x1E
    add 0b001, 3
// Empty lines are allowed

// Now a section with a jump
Label2:
    add 2, 2
    jmp Label1

Label3:
    nop
    jmp Label3