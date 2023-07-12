    .intel_syntax noprefix
    .text
    .global main

main:
    mov ebx , 3
    call wylicz
    add esp,4
    push eax
    mov eax , offset printf_arg1
    push eax
    call printf
    add esp , 8

exit:
    
    mov eax , 0
    ret

wylicz:
    cmp ebx,0 
    jne rek
    add eax,ecx
    ret 4

rek:
    dec ebx 
    add eax,eax 
    inc ecx 
    jmp wylicz
    

    .data
    printf_arg1:
    .asciz "%i"