/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    char s[20];
    scanf("%s",s);
    
    int i = 1;
    int num = 0;
    int answer = s[0] - '0';
    
    while(s[i] != '\0'){
        num = s[i] - '0';
        // printf("%d",num);
        if((num == 0) || (num == 1)||(answer == 0)||(answer == 1)){
            answer += num;
        }
        else{
            answer *= num;
        }
        i++;
    }
    
    printf("%d",answer);
}
