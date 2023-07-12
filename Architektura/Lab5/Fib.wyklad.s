# Argumenty do funkcji "fib" przekazywane przez stos;
# za zdjęcie argumentów ze stosu odpowiada wywołujący funkcję
#Wynik 1134903170
#
#real   0m6,558s
#user   0m6,552s
#sys    0m0,000s
    .intel_syntax noprefix
    .global main
    .text
main:
    mov eax, 45
    push eax
    call fib
    add esp, 4
    push eax
    mov eax, offset msg
    push eax
    call printf
    add esp, 8
    ret
fib:
    push ebp
    mov ebp, esp
    sub esp, 4
    # argument N: ebp+8
    # zmienna lokalna TMP: ebp-4
    mov eax, [ebp+8]
    cmp eax, 2
    ja rekurencja
    mov eax, 1
    jmp koniec
rekurencja:
    dec eax
    push eax
    call fib
    add esp, 4
    mov [ebp-4], eax
    mov eax, [ebp+8]
    dec eax
    dec eax
    push eax
    call fib
    add esp, 4
    add eax, [ebp-4]
koniec:
    mov esp, ebp
    pop ebp
    ret 

    ////

    # Argumenty do funkcji "fib" przekazywane przez stos;
# za zdjęcie argumentów ze stosu odpowiada wywoływana funkcja
#Wynik 1134903170


///
# Argumenty do funkcji "fib" przekazywane przez rejestr;
#Wynik 1134903170
#
#real   0m6,692s
#user   0m6,687s
#sys    0m0,000s
    .intel_syntax noprefix
    .global main
    .text
main:
    mov eax, 45
#   push eax
    call fib
#   add esp, 4


    push eax
    mov eax, offset msg
    push eax
    call printf
    add esp, 8
    
    ret
fib:
    push ebp
    mov ebp, esp
    sub esp, 8
    # argument N: ebp-8
    # zmienna lokalna TMP: ebp-4
    mov [ebp-8], eax
    cmp eax, 2
    ja rekurencja
    mov eax, 1
    jmp koniec
rekurencja:
    dec eax
#   push eax
    call fib
#   add esp, 4
    mov [ebp-4], eax
    mov eax, [ebp-8]
    dec eax
    dec eax
#   push eax
    call fib
#   add esp, 4
    add eax, [ebp-4]
koniec:
    mov esp, ebp
    pop ebp
    ret
    .data
msg:    .asciz "Wynik %i\n"


///


# Argumenty do funkcji "fib" przekazywane przez rejestr;
#Wynik 1134903170
#
#real   0m4,225s
#user   0m4,200s
#sys    0m0,000s
    .intel_syntax noprefix
    .global main
    .text
main:
    mov eax, 45
    call fib
    push eax
    mov eax, offset msg
    push eax
    call printf
    add esp, 8
    ret
fib:
    cmp eax, 2
    ja rekurencja
    mov eax, 1
    ret
rekurencja: 
    dec eax
    push eax
    call fib
    push eax    
    mov eax, [esp+4]
    dec eax
    call fib
    add eax, [esp]
    add esp, 8
    ret
    .data
msg:    .asciz "Wynik %i\n"


///
#include <stdio.h>
int fib(int n) {
    return (n <=2 ? 1 : fib(n-1)+fib(n-2));
}
int main() {
    printf("Wynik %i\n", fib(45));
}