#include <stdio.h>
#include <cs50.h>
int main()
{
    int a=0;
    int height = get_int("Height :");
    for (int i=0; i < height ;i++)
    {
        for (int l=0; l < height-i; l++)
        {
            printf(" ");
        }
        for (int z=0; z<i+1; z++)
        {
            printf("#");
        }
        if (a==0)
        {
            printf(" ");
        }
        for (int z=0; z<i+1; z++)
        {
            printf("#");
        }

        printf("\n");
    }
return 0;
}