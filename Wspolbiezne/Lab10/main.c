//gcc -fopenmp -o main main.c -lm
#include <omp.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define MLD 1000000000.0
#define N 1000000

bool is_prime(int num){
    if (num < 2)
        return false;

    int limit = (int)sqrt(num);
    for (int i = 2; i <= limit; i++){
        if (num % i == 0)
            return false;
    }
    return true;
}

int main(){
    int num_threads;
    printf("Podaj ilosc watkow: ");
    scanf("%d", &num_threads);

    struct timespec tp0, tp1;
    double Tn;
    int prime_count = 0;
    int *primes = (int *)malloc(N * sizeof(int));

    omp_set_num_threads(num_threads);

    clock_gettime(CLOCK_MONOTONIC, &tp0);

#pragma omp parallel
        {
        int thread_count = omp_get_num_threads();
#pragma omp for
        for (int i = 2; i <= N; i++){
            if (is_prime(i)){
#pragma omp critical
                {
                    primes[prime_count] = i;
                    prime_count++;
                }
            }
        }
#pragma omp single
        {
            printf("Uzyto %d watkow\n", thread_count);
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &tp1);

    Tn = (tp1.tv_sec + tp1.tv_nsec / MLD) - (tp0.tv_sec + tp0.tv_nsec / MLD);

    printf("Liczba znalezionych liczb pierwszych: %d\n", prime_count);
    printf("Czas: %lf sekund\n", Tn);

    free(primes);

    return 0;
}