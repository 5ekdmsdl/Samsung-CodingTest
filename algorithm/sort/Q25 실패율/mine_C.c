/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
int count(int* stages, int target, int n){
    int cnt = 0;
    for(int j=0;j<n;j++){
            if(stages[j] == target){
                cnt ++;
            }
        }
    return cnt;
}

int compare(int*a, int*b){
    return *(int*)a - *(int*)b;
}


int main()
{
    int n = 5;
    int stages[8] = {2,1,2,6,2,4,3,3};
    double** perc;
    int total = sizeof(stages)/sizeof(int);
    perc = (double**) malloc(sizeof(double*)*n);
    
    int* answer;
    answer = (int*)malloc(sizeof(int)*n);
    
    for(int i=0;i<n;i++){
        perc[i] = (double*) malloc(sizeof(double)*2);
    }
    
    
    for(int i=0;i<n;i++){
        int target = i+1;
        int now = count(stages,target,sizeof(stages)/sizeof(int));
        
        printf("%d\n\n",now);
        
        perc[i][0] = (double)now / total;
        perc[i][1] = target;
        
        total -= now;
    }
    
    perc = qsort(perc,sizeof(perc)/(sizeof(int)*2),sizeof(int),compare);
    
    for(int i=0;i<n;i++){
        answer[i] = perc[i][1];
    }
    

    for(int i=0;i<n;i++){
        // for(int j=0;j<2;j++){
        //     printf("%f  ",perc[i][j]); 
        // }
        printf("%d  ",answer[i]);
        printf("/");
    }
}
