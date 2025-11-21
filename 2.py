#include <stdio.h>

int main() {
    int data[50], div[20], rem[20];
    int datalen, divlen;
    int i, j, k, ch;

    printf("Enter the data (binary): ");
    i = 0;
    while ((ch = getchar()) != '\n') {
        data[i++] = (ch == '1') ? 1 : 0;
    }
    datalen = i;

    printf("Enter the divisor (binary): ");
    i = 0;
    while ((ch = getchar()) != '\n') {
        div[i++] = (ch == '1') ? 1 : 0;
    }
    divlen = i;

    // Append zeros
    for (i = datalen; i < datalen + divlen - 1; i++)
        data[i] = 0;

    int total_len = datalen + divlen - 1;

    // Copy first divisor length bits into remainder
    for (i = 0; i < divlen; i++)
        rem[i] = data[i];

    k = divlen - 1;

    while (k < total_len) {
        if (rem[0] == 1) {
            for (i = 0; i < divlen; i++)
                rem[i] = rem[i] ^ div[i];
        }

        // Shift Left
        if (k == total_len - 1) break;

        for (i = 0; i < divlen - 1; i++)
            rem[i] = rem[i + 1];

        rem[i] = data[++k];
    }

    // Store remainder back into data
    j = 1;
    for (i = total_len - (divlen - 1); i < total_len; i++)
        data[i] = rem[j++];

    printf("\nFinal data to be sent (CRC encoded): ");
    for (i = 0; i < total_len; i++)
        printf("%d", data[i]);

    printf("\n");
    return 0;
}