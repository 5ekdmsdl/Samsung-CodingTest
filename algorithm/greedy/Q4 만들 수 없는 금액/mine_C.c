/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

int compare(const void*a, const void*b){
    return *(int*)a - *(int*)b;    
}

int find_idx(int target,int* coins,int n){
    for(int i = 0;i<n;i++){
        if(coins[i] > target){
            return i-1;
        }
    }
    return n-1;
}

int main()
{
    int n = 0;
    // char line[1000];
    
    // int coins[1000];
    int *coins = malloc(sizeof(int) * 1000);
    
    scanf("%d",&n);
    // gets(line);
    
    // int i = 0;
    // while(line[i] != '\0'){
    //     if(line[i] == ' '){
    //         continue;
    //     }
    //     coins[i] = line[i] - '0';
    // }
    for(int i=0;i<n;i++){
        scanf("%d",&(coins[i]));
    }
    
    printf("%d\n",sizeof(coins)/sizeof(int));
    qsort(coins,sizeof(coins)/sizeof(int),sizeof(int),compare);
    
    for(int i=0;i<n;i++){
        printf("%d\n",coins[i]);
    }
    
    int idx;
    int target;
    char flg = 0;
    
    for(int i = 1; flg == 0; i++){
        target = i;
        idx = find_idx(target,coins,n);
        while(1){
            if(idx < 0){
                flg = 1;
                printf("%d",i);
                break;
            }
            if(target == coins[idx]){
                break;
            }
            else{
                target = target - coins[idx];
                idx--;
            }
        }
        
        
    }
}
