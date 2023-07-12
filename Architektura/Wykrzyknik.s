.intel_syntax noprefix 
.text
.global main

main:
    mov eax, offset messg
    push eax
    call znajdz
    add esp, 4
    push eax
    mov eax , offset printf_arg1
    push eax
    call printf
    add esp, 8

exit:
    mov eax, 0
    ret

znajdz:
    mov eax,0
    push eax
    mov eax,0
    push eax
    jmp search

finish:  ;#ilosc znakow do wykrzyknika
    mov eax,[esp]
    dec eax
    add esp,8
    ret
search:
    mov eax,[esp + 12] 
    add eax,[esp] 
    mov eax,[eax]

    mov eax,[esp+4]
    cmp eax,4
    je finish

    mov eax,[esp + 12] 
    add eax,[esp]
    mov eax,[eax]

    cmp eax,0
    je finish

    cmp al,'!'
    je found

    pop eax
    inc eax
    push eax

    jmp search

found:
    mov eax,[esp+4]
    inc eax
    mov [esp+4],eax

    pop eax
    inc eax
    push eax

    jmp search    
    
    

.data
messg:
    .asciz "Prz!y!!kl!adowy!ekst"
printf_arg1:
    .asciz "%i\n"

