#include<math.h>
#include<stdio.h>

int main(){
  int i, sum;
  for(i = 1; i<=100000; i++)
    sum = i*i + sum;
  printf("%d\n", sum);
}
