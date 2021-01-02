#include<stdio.h>
#include<stdlib.h>

int main(){
  int* a;
  int i, j;
  int N = 30;

  a = (int*)malloc(N * sizeof(int));

  a[0] = 43;
  for(i = 1; i < N; i++){
    a[i] = (a[i-1] * 17 + 13) % 100;
}

i = 0;
int sum = a[i];
while(sum<=1000){
  sum+=a[++i];
 }

for(j = 0; j<= i; j++)
  printf("%d ", a[j]);
printf("Sum = %d/n", sum);

for(i = 0; i<N; i++){
  if(*(a+i)<10)
    printf("a[%d] = %d\t", i, a[i]);
 }
printf("\n");
}
