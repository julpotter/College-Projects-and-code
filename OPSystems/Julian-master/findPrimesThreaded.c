#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<pthread.h>

/*
 * Forward declarations of some functions 
 */
int isPrime(int N);
void* countSomePrimes(void* work);

typedef struct thread_work{
  int start;
  int end;
} thread_work;

int count;            // Global count, accessible to main and all threads
pthread_mutex_t count_mutex;

int main(int c, char* argv[]){
  // Read the commandline arguments
  int N = atoi(argv[1]);	/* Find primes from 1 to N */

  count = 0;
  pthread_mutex_init(&count_mutex, NULL)
  int num_threads = 12000;
  pthread_t intsT[num_threads];	/* Array of thread ids, for joining later */
  thread_work w[num_threads];	/* Array of work structures, one per thread */
  int start, end;

  for(int i = 0; i < num_threads; i++){
    start = 1 + (i*N)/num_threads;
    end = (i+1)*N/num_threads;
    w[i].start = start;
    w[i].end = end;
  
    pthread_create(&intsT[i], NULL, countSomePrimes, (void*)&w[i]);
  }

  // We have to pause the master thread until all workers finish
  for(int i = 0; i < num_threads; i++){
    pthread_join(intsT[i], NULL);
  }

  printf("There are %d primes between 1 and %d\n", count, N);
}

void* countSomePrimes(void* work){
  thread_work *w = (thread_work*)work;

  int start = w->start;   	/* Reach inside a pointed-to struct and get data from it */
  int end = w->end;

  for(int i = start; i <= end; i++){
    if isPrime(N){
	pthread_mutex_lock(&count_mutex);
	count++;
	pthread_mutex_unlock(&count_mutex);
		}


/*
 * Returns true if the number is a prime >= 2
 * and false otherwise.
 *
 * In C, "0" means "false," "not 0" means "true".
 */
int isPrime(int N){
  if(N == 2)
    return 1;

  if(N < 2 || (N % 2) == 0)
    return 0;

  int i;			/* counter */
  for(i = 3; i <= sqrt(N); i = i + 2){
    if(N % i == 0)
      return 0;
  }

  return 1;			/* If we make it here, N has no divisors */
}
