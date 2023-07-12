.intel_syntax noprefix
.text
.global main

main:
    mov ecx, 3
    push ecx
    call wylicz
    add esp, 4
    push eax
    mov eax, offset printf_arg1
    push eax
    call printf
    add esp, 8

exit:
    mov eax, 0
    ret

wylicz: ;# Program do liczena rekurencji
    mov eax, [esp+4]
    cmp ecx, 0
    ja rek
    add eax, eax 
    ret

rek:
    dec ecx
    add eax, 3
    push eax
    call wylicz
    add esp, 4
    inc eax
    ret


    .data
printf_arg1:
    .asciz "%i\n"