#include <stdio.h>
//chcemy napisac ./a.out 10 
//I chcemy otrzymac 2*10 czyli 20
int main {int ARGC, char **ARCV}{
    char *arg1 = ARGV[1]; //ARGV[0] to nazwa programu 
    int x = atoi(arg1); //atoi zamienia liczbe na ciag znakow
    return 2*x;
}