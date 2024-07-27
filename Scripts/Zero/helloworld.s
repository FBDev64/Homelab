.global _start
_start:
    mov r7, #4
    ldr r1, =msg
        ldr r0, =len
    mov r7, #1
    swi 0

.data
    msg:
      .asciz "Hello, ARM\n"
    len = .-msg