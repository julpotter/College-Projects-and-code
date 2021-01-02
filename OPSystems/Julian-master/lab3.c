/*
  Finish this code so that it:

  * Builds a doubly-linked list of pte structures, with random integer ages from 1 to 100
  * Prints the ages, in order from left to right, in the list
  * Bubble sort the doubly-linked list, by age
  * Print them again, so we can see they're sorted.

  Starter code is below

  ------------------------------

  Bubble Sort a doubly-linked list
*/

#include<stdio.h>
x = random()%100 + 1;
printf(x);

typedef struct pte{
  int pageID;
  struct pte *prev;
  struct pte *next;
  int age;
} pte;

#define N 100 /* Number of pages */

int main(){
  int i; /* counter */
  pte *first; /* "first" entry in the ring */
  pte *iter; /* Iterator around the ring */

  first = (pte*)malloc(sizeof(pte));
  first->pageID = 0;
  first->age = 0;

  // Build the doubly-linked list of ptes
  iter = first;
  for(i = 0; i < N; i++){
    pte *p = (pte*)malloc(sizeof(pte));

   
    iter->next = p;
    p->prev = iter;
    p->pageID = iter->pageID + 1;
    p->age = random()%100 + 1;  //randomly generate ages
    iter = p;
    

  }

  // Print the ages, in order, in the list
  while(p->next != NULL){
    p = first;
    printf("%d\n",p->age);
    p = p->next;
    printf("%d\n",p->age);
    
  }
  // Bubble sort the list
  for(i=0; i<N; i++){
    if(p->age > p->age->next){
      p->age->prev = p->age;
      p->age = p->age->next;
      p->age->next = p->age->next->next;
    }
  }
  // Print sorted ages
  while(p->next != NULL){
    p = first;
    printf("%d\n",p->age);
    p = p->next;
    printf("%d\n",p->age);

  }
  return 0;
}
