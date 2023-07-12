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

    dec eax           ;# eax = 9

    call fib          ;# eax=fib(9)

    mov [ebp-4], eax  ;# [ebp-4] = eax ,czyli [ebp-4] = fib(9)
                      
    mov eax, [ebp-8]  ;# eax = 10
    dec eax           ;# eax = 9
    dec eax           ;# eax = 8

    call fib          ;# eax = fib(8)

    add eax,eax       ;# eax = fib(8) + fib(8) = 2 * fib(8)
    add eax,[ebp-4]   ;# eax = 2 * fib(8) + fib(9)
    mov [ebp-4],eax   ;# [ebp-4] = eax, czyli [ebp-4] = 2 * fib(8) + fib(9)

    mov eax,[ebp-8]   ;# eax = 10
    dec eax           ;# eax = 9
    dec eax           ;# eax = 8
    dec eax           ;# eax = 7
    
    call fib          ;# eax = fib(7)

    add eax,[ebp-4]   ;# eax = fib(7) + 2 * fib(8) + fib(9)
    
    leave
    ret

    .data
msg:    .asciz "Wynik %i\n"