#include <stdio.h> 

int main (){

    char s[] = "abcde xyz";

asm (
        ".intel_syntax noprefix;"
        

        "mov eax,%0\n"   //do liczenia dlugosci stringa
        "mov esi,0\n"   //poczatek napisu
        "mov edi,0\n"  //koniec napisu
        "mov ecx,0\n" //licznik
        "mov esi,eax\n"
        
    "Dlugosc_stringa:"

        "mov bl,[eax]\n" 
        "cmp bl,0\n"

        "je tutaj\n"

        "inc eax\n" 
        "inc ecx\n"

        "jmp Dlugosc_stringa\n"
        

    "tutaj:"
        "mov edi,eax\n" //tutaj eax pokazuje na "wartownika", wiec linijke nizej decrementuje edi aby pokazywal na ostatni znak napisu
        "dec edi\n"
        
    "petla:"

        "mov al,[esi]\n"
        "mov bl,[edi]\n"
        "mov [esi],bl\n"
        "mov [edi],al\n"
        
        "inc esi\n"
        "dec edi\n"
        "sub ecx,2\n"
        
        "cmp ecx,1\n"
        "jg petla\n" // jesli ecx > 0 to skok do petli
        

        ".att_syntax prefix;"
    :
    : "r" (s)
    : "eax", "ecx", "edi", "esi", "al", "bl"
    );
   
    printf("Wynik: %s\n",s);
    return 0;
}