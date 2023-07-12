	.file	"Test.c"
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "Wynik: %s\12\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB10:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%edi
	pushl	%esi
	pushl	%ebx
	andl	$-16, %esp
	subl	$32, %esp
	.cfi_offset 7, -12
	.cfi_offset 6, -16
	.cfi_offset 3, -20
	call	___main
	movl	$1684234849, 27(%esp)
	movb	$0, 31(%esp)
	leal	27(%esp), %edx
/APP
 # 7 ".\Test.c" 1
	.intel_syntax noprefix;mov eax, %edx
mov esi, 0
mov edi, 0
mov ecx, 0
mov esi,eax
Dlugosc_stringa:mov al,[eax]
cmp al,0
je tutaj
inc eax
inc ecx
jmp Dlugosc_stringa
tutaj:mov edi,eax
dec edi
petla:mov al, [esi]
mov bl, [edi]
mov [esi], bl
mov [edi], al
inc esi
dec edi
sub ecx,2
cmp ecx,1
jg petla
.att_syntax prefix;
 # 0 "" 2
/NO_APP
	leal	27(%esp), %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leal	-12(%ebp), %esp
	popl	%ebx
	.cfi_restore 3
	popl	%esi
	.cfi_restore 6
	popl	%edi
	.cfi_restore 7
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE10:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
