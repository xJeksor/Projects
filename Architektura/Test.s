.intel_syntax noprefix
.text
.global main


main:
    mov eax, 5
    push eax
    mov eax 7
    push eax
    mov eax 9
    push eax
    add esp,4
    mov eax,[esp-4]
    add esp,8
    push eax
    mov eax , offset printf_arg1
    push eax
    call printf
    add esp, 8

.data

printf_arg1:
    .asciz "%i\n"

