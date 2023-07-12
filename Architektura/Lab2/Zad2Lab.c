#include <stdio.h> //komentarze zostawiam dla siebie na przyszlosc :) 

int main (){

int x = 0xFFFFFFFF; 
int y;

asm ( 
".intel_syntax noprefix;"
"mov eax, %1\n" // x = eax ,ecx = tymczasowy max, edx = max
"mov ebx,32\n" // ebx = licznik
// "mov ecx, %0\n" //zeruje ecx bo y = 0 (nwm czy tak mozna)
// "mov edx, %2\n" 
"xor ecx,ecx\n"
"xor edx,edx\n"

"petla:"
"shl eax\n" //przesun w lewo
"jnc skok1\n" //jezeli nie jest 0 to idz do linijki nizej jak jest 0 to idz do skok1
"inc ecx\n" 
"cmp edx,ecx\n" // odejmij od maxa -> tymczasowego maxa ale nie zapisuj wyniku ( mimo to flagi nam sie ustawią )
"jns skok2\n" //to sie wykona czyli skoczy do skok2 jesli edx - ecx > 0
"mov edx,ecx\n"  
"cmp edx,100\n"
"js skok2\n" 

"skok1:"
"mov ecx,0\n"
"dec ebx\n"
"jnz petla\n"
"cmp edx,100\n"
"js koniec\n"

"skok2:"
"dec ebx\n"
"jnz petla\n"
"mov %0,edx\n"

"koniec:"
"mov %0,edx\n"


".att_syntax prefix"
: "=r" (y)
: "r"  (x)
: "eax" ,"ebx","ecx","edx"
);

printf("Wynik %i\n",y);

return 0;
}
