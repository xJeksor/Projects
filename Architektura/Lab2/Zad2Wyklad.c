#include <stdio.h>

int main() {
    int x = 2021;
    int y = 0;
    asm (
        ".intel_syntax noprefix;"
        "mov eax, %1;"
        "mov ebx, eax;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "add eax, ebx;"
        "mov %0, eax;"
        ".att_syntax prefix;"
    : "=r" (y)
    : "r" (x)
    : "eax", "ebx"
    );

    printf("Argument %i\nWynik %i\n", x,y);
    return 0;
}