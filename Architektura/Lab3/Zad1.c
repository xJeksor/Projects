#include <stdio.h> // zad dom tak samo jak to ale efekt : odwrocenie lancucha znakow zamiast powiekszenie o jeden, czyli  abc -> cba
// wykorzystac kod aby znalezc dlugosc lancucha potem pierwszy rejestr 0 a drugi rejestr dlugosc -1  i zamienic te rejestry potem rejestr pierwszy zwiekszam o 1 a ostatni zmiejszam o 1 i sprawdzic czy sie nie zamienia miejscami  

int main (){

    char s[] = "abc";

     asm (
        ".intel_syntax noprefix;"

        "mov ebx,%0\n"
        

        "petla:"
        "mov al,[ebx]\n"

        "cmp al, 0;"
        "je koniec;"

        "inc al\n"
        "mov [ebx],al\n"
        "inc ebx\n" 
        "jmp petla\n"
        "koniec:"

        
        ".att_syntax prefix;"
    :  
    : "r" (s) 
    : "ebx", "al" 
    );
    printf("Wynik: %s",s);
    return 0;
}