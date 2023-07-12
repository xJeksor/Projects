    .intel_syntax noprefix

    .global main

    .text

main:

    mov eax,[esp + 8]
    mov ebx,[eax + 4]

    push ebx
    call atoi
    add esp,4

    add eax,eax

    ret