    .intel_syntax noprefix
    .text
    .global main

main:
    mov ebx , 2
    push ebx
    inc ebx
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
    mov eax,[esp+4]  
    cmp ebx,1
    ja rek
    add eax,[esp+12]
    ret

rek:
    dec ebx
    add eax,eax
    call rek2
    add esp,4
    call wylicz
    add esp,4
    ret

rek2: 
    add eax,1
    push eax
    ret

  .data
    printf_arg1:
    .asciz "%i"   