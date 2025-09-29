section .data
    num1 dq 5
    num2 dq 3
    msg1 db "Sum = ",0
    msg2 db "Product = ",0
    newline db 10,0
    buffer db 20 dup(0)

section .text
    global _start

_start:
    mov rax, [num1]
    add rax, [num2]
    mov rsi, msg1
    call print_cstring
    mov rsi, buffer
    call int_to_string
    call print_cstring
    mov rsi, newline
    call print_cstring

    mov rax, [num1]
    imul rax, [num2]
    mov rsi, msg2
    call print_cstring
    mov rsi, buffer
    call int_to_string
    call print_cstring
    mov rsi, newline
    call print_cstring

    mov rax, 60
    xor rdi, rdi
    syscall

print_cstring:
    push rsi
    xor rcx, rcx
.count:
    cmp byte [rsi + rcx], 0
    je .done
    inc rcx
    jmp .count
.done:
    mov rdx, rcx
    pop rsi
    mov rax, 1
    mov rdi, 1
    syscall
    ret

int_to_string:
    mov rbx, 10
    mov rcx, buffer
    add rcx, 19
    mov byte [rcx], 0
.convert:
    xor rdx, rdx
    div rbx
    add dl, '0'
    dec rcx
    mov [rcx], dl
    test rax, rax
    jnz .convert
    mov rsi, rcx
    ret
