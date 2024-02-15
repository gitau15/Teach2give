//Fibonacci sequence
#include <stdio.h>
int main(){

int i,n3;
int n1=0;
int n2=1;
printf("\n%d\n%d",n1,n2);

for(i=0;i<10;i++){
    n3=n1+n2;
    printf("\n%d",n3);
n1=n2;
n2=n3;
}

return 0;
}