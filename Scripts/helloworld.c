#include <stdio.h>

int main() {
    char msg[] = "Hello, ARM\n";
    int len = sizeof(msg) - 1;
    write(STDOUT_FILENO, msg, len);
    return 0;
}

// Converted with a codeconvert.ai/assembly-to-c-converter