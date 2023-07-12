#include <stdio.h> // zad dom tak samo jak to ale efekt : odwrocenie lancucha znakow zamiast powiekszenie o jeden, czyli  abc -> cba
// wykorzystac kod aby znalezc dlugosc lancucha potem pierwszy rejestr 0 a drugi rejestr dlugosc -1  i zamienic te rejestry potem rejestr pierwszy zwiekszam o 1 a ostatni zmiejszam o 1 i sprawdzic czy sie nie zamienia miejscami  

int main (){

    char s[] = "ab";

     asm (
        ".intel_syntax noprefix;"

        "mov ebx,%0\n"
        "mov ecx,0\n"

        "Dlugosc_stringa:"

        "cmp [ebx],0\n"
        "je tutaj\n"

        "inc ebx\n" 

        "cmp [ebx],0\n"
        "je tutaj\n"

        "inc ecx\n"

        "jmp Dlugosc_stringa\n"
        
        "tutaj:"
        "dec ebx\n"
        "mov edx,ebx\n" // edx wskazuje na koniec lancucha, a ebx na poczatek
        "mov ebx,%0\n"
        "mov al,ebx\n"

        "petla:"
        "cmp ecx,0\n"
        "je koniec\n"

        "mov al,[edx]\n"
        "mov bl,[ebx]\n"
        //"sub ecx,2\n"
        "dec edx\n"
        "inc ebx\n"
        "mov cl,[edx]\n"
        "mov dl,[ebx]\n"
        "koniec:"

        
        ".att_syntax prefix;"
    :  
    : "r" (s) 
    : "edx","ecx","ebx", "al" , "bl" 
    );
    printf("Wynik: %s",s);
    return 0;
}



//  "mov al, [ebx]\n"
//         "cmp al, 0\n"
//         "je koniec\n"
//         "inc al\n"
//         "mov [ebx],al\n" // bbc ,
//         "inc ebx\n"
//         "inc ecx\n"
//         "jmp petla\n"

//         "cmp al, 0;"
//         "je koniec;"

//         "inc al\n"
//         "mov [ebx],al\n"
//         "inc ebx\n" 
//         "jmp petla\n"