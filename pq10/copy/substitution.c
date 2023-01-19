#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main(int argc, string argv[])
{
    //string c = get_string("plaintext: ");
    //int q = strlen(c);
    //printf("\n");


   if (argc != 2)
   {
        printf("Usage: ./substitution key\n");
        return 1;
   }

   int l = strlen(argv[1]);

   if (l != 26)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }


    for (int i = 0; i < l; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    }


    for (int i = 0; i < l; i++)
    {
        if (!((argv[1][i] >= 'a' && argv[1][i] <= 'z') || (argv[1][i]>= 'A' && argv[1][i] <= 'Z')))
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    }


    for (int i = 0; i < l; i++)
    {
        for(int j = i+1; j < l; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                printf("Usage: ./substitution key\n");
                return 1;
            }
        }
    }


    string plain = get_string("plaintext: ");
    printf("ciphertext: ");
    int x = strlen(plain);
    for (int i = 0; i < x; i++)
    {
        if (isupper(plain[i]))
        {
            printf("%c", toupper(argv[1][plain[i] - 65]));
        }
        else if (islower(plain[i]))
        {
            printf("%c", tolower(argv[1][plain[i] - 97]));
        }
        else
        {
            printf("%c", plain[i]);
        }

    }
    printf("\n");
}