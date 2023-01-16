//Check for hyperv environment by CPUID
int IsVirtualized() {
    int result = 0;
    __try {
        __asm {
            push eax
            mov eax, 1
            cpuid
            test edx, 0x80000000
            jz not_virtualized
            mov eax, 0
        not_virtualized:
            pop eax
        }
    } __except (EXCEPTION_EXECUTE_HANDLER) {
        result = 1;
    }
    return result;
}

section .data
    server db "127.0.0.1",0   ; IP address of the server
    port dw 80               ; Port number to connect to

section .text
    ; Create a socket
    mov eax, 2        ; socket() syscall number
    mov ebx, 1        ; AF_INET (IPv4)
    mov ecx, 1        ; SOCK_STREAM (TCP)
    mov edx, 0        ; Protocol (default)
    int 0x80          ; Call kernel

    ; Connect to the server
    mov eax, 3        ; connect() syscall number
    mov ebx, eax      ; File descriptor returned by socket()
    mov ecx, server   ; Pointer to server address
    mov edx, 2        ; Size of server address (16 bits)
    int 0x80          ; Call kernel