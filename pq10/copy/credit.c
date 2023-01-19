#include <stdio.h>
#include <cs50.h>
int main()
{
    long num=get_long("Number: ");
    int i=0;
    long cred=num;
    while (cred>0)
    {
        cred=cred/10;
        i++;
    }
    if (i!=13 && i!=15 && i!=16)
    {
        printf("INVALID\n");
    }
    int sum_1=0,sum_2=0,total=0;
    long x=num;
    int mod_1,mod_2,d1,d2;
    do
    {
        mod_1=x%10;
        x=x/10;
        sum_1=sum_1+mod_1;
        mod_2=x%10;
        x=x/10;
        mod_2=mod_2*2;
        d1=mod_2%10;
        d2=mod_2/10;
        sum_2=sum_2+d1+d2;
    }
    while (x>0);
    total =sum_1+sum_2;
    if (total%10 !=0)
    {
        printf("INVALID\n");
        return 0;
    }
    long start=num;
    do
    {
        start=start/10;
    }
    while (start>100);
    if ((start/10==5) && (0<start%10 && start%10 <6))
    {
        printf("MASTERCARD\n");
    }
    else if ((start/ 10==3) && (start% 10== 4 || start% 10==7))
    {
        printf("AMEX\n");
    }
    else if (start/ 10==4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
return 0;
}