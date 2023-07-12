    .intel_syntax noprefix
    .global main
    .text
main:
    mov eax, 10         

    call fib

    push eax  
    mov eax, offset msg
    push eax
    call printf
    add esp, 8
    
    ret
fib:
    cmp eax, 3
    ja rekurencja

    mov eax, 1
    ret

rekurencja:
    push ebp          
    mov ebp, esp

    sub esp, 8

    # argument N: ebp-8
    # zmienna lokalna TMP: ebp-4
    
    mov [ebp-8], eax

    dec eax           ;# eax = N-1

    call fib          ;# eax = fib(N-1)

    mov [ebp-4], eax  ;# [ebp-4] = eax ,czyli [ebp-4] = fib(N-1)
                      
    mov eax, [ebp-8]  ;# eax = N
    dec eax           ;# eax = N-1
    dec eax           ;# eax = N-2

    call fib          ;# eax = fib(N-2)

    add eax,eax       ;# eax = 2 * fib(N-2)
    add eax,[ebp-4]   ;# eax = 2 * fib(N-2) + fib(N-1)
    mov [ebp-4],eax   ;# [ebp-4] = eax, czyli [ebp-4] = 2 * fib(N-2) + fib(N-1)

    mov eax,[ebp-8]   ;# eax = N
    dec eax           ;# eax = N-1
    dec eax           ;# eax = N-2
    dec eax           ;# eax = N-3
    
    call fib          ;# eax = fib(N-3)

    add eax,[ebp-4]   ;# eax = fib(N-3) + 2 * fib(N-2) + fib(N-1)
    
    leave
    ret

    .data
msg:    .asciz "Wynik %i\n"