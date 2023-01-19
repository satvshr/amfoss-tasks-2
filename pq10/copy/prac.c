// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int A[5];
    int i, z;
    for (i=0; i<5; i++)
    {
        printf("Enter the elements:");
        scanf("%d",&A[i]);
    }

    for (i=0; i<5; i++)
    {
        for (z=0; z<5; z++ )
        {
            if ((A[i]+A[z])%2 == 0)
            {
                printf("%d,%d are a pair ",A[i],A[z]);
            }
        }
    }   

    return 0;
}