section     .text
global      _start
_start:
    mov     edx,len
    mov     ecx,msg
    mov     ebx,1
    mov     eax,4
    int     0x80
    mov     eax,1
    int     0x80
section     .data
msg     db  'Hello world',0xa
len     equ $ - msg

; how to run:
; 1. fist install assemblers
; sudo apt install as31 nasm
; 2. assemble the program
; nasm -f elf64 x86_assembly.asm
; 3. link the object file into an executable file
; ld -s -o x86_assembly x86_assembly.o
; 4. execute it
; ./x86_assembly
