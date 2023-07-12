    .intel_syntax noprefix

    .global main

    .text

main:

    mov eax,[esp + 4]
    dec eax
    ret