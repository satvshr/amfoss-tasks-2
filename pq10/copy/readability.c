#include <stdio.h>
#include <math.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>
int main()
{
    string txt = get_string("Text: ");
    printf("%s\n",txt);
    int letters = 0;
    int l = strlen(txt);
    for (int i=0; i < l; i++)
    {
        if ((txt[i] >= 'a' && txt[i] <= 'z') || (txt[i]>= 'A' && txt[i] <= 'Z'))
        {
            letters++;
        }
    }
    printf("%i\n", letters);

    int words = 1;
    for (int i=0; i < l; i++)
    {
        if (txt[i]==' ')
        {
            words++;
        }
    }
    printf("%i\n", words);
    float W = words/100.0;
    int sentences = 0;
    for (int i=0; i < l; i++)
    {
        if ((txt[i]=='.') || (txt[i]=='?') || (txt[i]=='!'))
        {
            sentences++;
        }
    }
    printf("%i\n", sentences);
    float L = letters / W;
    float S = sentences / W;
    float index = index = 0.0588 * L - 0.296 * S - 15.8;
    int V = round(index);

    if (V > 16)
    {
        printf("Grade 16+\n");
    }
    else if (V < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("The grade is:%i\n", V);
    }
}





