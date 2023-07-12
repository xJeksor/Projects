#include <stdio.h>

int main (){

int x = 0xFFFFFFFF; //jezeli zaczyna sie 0x to system 16-stkowy, binarnie ta liczba to : 0110 0111 0100 0000 1111 0000 0000 0000 -> ilosc jedynek to 10
int y;
//program liczy ilosc jedynek w liczbie binarnej i zwieksza ecx, czyli nasz wynik o jeden jezeli w fladze c natrafimy na jedynke
//zamiast ; lepiej uzywac \n na koncu dzieki temu jak bedzie blad to uzywajac \n dostaniemy konkretna linie w ktorej jest blad a gdybysmy uzywali ; to wszystko liczy sie jako jedna linia
asm ( 
".intel_syntax noprefix;"
"mov eax, %1\n"// %1 to x, rejestry ustawiane sa od gory do dolu,od lewej do prawej
"mov ebx,32\n" //ebx = nasz licznik
"mov ecx,0\n" //operacja xor jest idealna do zerowania (bo 00->0, 11->0) wiec mozna zapisac xor ecx,ecx;
"petla:"
"shl eax\n" //shl = shift left
"jnc skok\n" //jnc = jump not c (flaga carry)
"add ecx,1\n" //add = dodaj mozna zapisac inc(increment = dodaj 1) ecx;
"skok:"
"sub ebx,1\n" //sub = odejmij mozna zapisac dec(decrement = odejmij 1) ebx;
"jnz petla\n" //jnz = jump not z (flaga zero)
"mov %0,ecx\n" // do %0 czyli x zaladuj wartosc z ecx    
".att_syntax prefix"
: "=r" (y) //Pierwszy ":" mowi co nasz program wyprowadza/modyfikuje, =r oznacza register(moze byc jeszcze =m to wtedy bysmy chcieli zeby y byl w pamieci), w tym przypadku chcemy ustawic/zmodyfikowac y,jezeli chcemy wiecej zmiennych modyfikowac to trzeba je tutaj wypisac po przecinku np. "=r" (y),"=r" (x), itd...  (nie mozna ogolnie uzyc za duzo rejestrow)
: "r" (x)   //Drugi ":" mowi o tym czego oczekujemy na wejsciu, czyli co spodziewamy sie ze kompilator przygotuje, my spodziewamy sie ze przygotuje nam x
: "eax", "ebx", "ecx" //Trzeci ":" mowi o skutkach ubocznych naszej wstawki, czyli informacja jakie rejestry sa zmodyfikowane(pozwala to uniknac sytuacji gdzie losowa zmienna ktorej nie uzywamy zmienilaby wartosc co jest niedopuszczalne), gdybysmy zrobili blad i nie napisali tutaj rejestru jakiegos a zmodyfikowali jego wartosc no to moglo by dojsc do sytuacji ze uzylibysmy czegos co jest juz wykorzystawane,czyli zniszczylibysmy jakos wartosc przez to program zaczalby dzialac w sposob przypadkowy co wiecej przy jednek kompilacji moglby zadzialac dobrze a po kilku latach na innej wersji zle
);

printf("Wynik %i\n",y);

return 0;
}


