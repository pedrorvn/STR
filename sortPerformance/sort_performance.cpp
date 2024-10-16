#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

// Vetores usados pelos métodos de ordenação
int *vetorQuickSort;
int *vetorBubbleSort;

// Função usada pelo qsort para comparar dois números
int compare_ints(const void* a, const void* b) {
    int* arg1 = (int*) a;
    int* arg2 = (int*) b;
    if (*arg1 < *arg2) return -1;
    else if (*arg1 == *arg2) return 0;
    else return 1;
}

// Algoritmo de ordenação bubble sort
void bubbleSort(int* vetor, int tamanho) {
    int aux;
    for (int i = 0; i < tamanho - 1; i++) {
        for (int j = 0; j < tamanho - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
}

// Função para criar os vetores de teste
void criarVetor(int tamanhoVetor, int semente) {
    srand(semente);
    vetorQuickSort = new int[tamanhoVetor];
    vetorBubbleSort = new int[tamanhoVetor];
    for (int i = 0; i < tamanhoVetor; i++) {
        vetorQuickSort[i] = rand() % 100000;
        vetorBubbleSort[i] = vetorQuickSort[i]; // usar os mesmos valores
    }
}

int main() {
    // Vetores com diferentes tamanhos para testar
    int tamanhos[] = {20000, 40000, 60000, 80000, 100000};
    int numTestes = 5;
    struct timeval tempo_inicial, tempo_final;
    int tmili;

    for (int i = 0; i < numTestes; i++) {
        int n = tamanhos[i];
        printf("\nTestando com vetor de tamanho: %d\n", n);
        
        // Criar o vetor com os valores aleatórios
        criarVetor(n, 23);
        
        // Medir o tempo do QuickSort
        gettimeofday(&tempo_inicial, NULL);
        qsort(vetorQuickSort, n, sizeof(int), compare_ints);
        gettimeofday(&tempo_final, NULL);
        tmili = (int) (1000 * (tempo_final.tv_sec - tempo_inicial.tv_sec) + (tempo_final.tv_usec - tempo_inicial.tv_usec) / 1000);
        printf("Tempo QuickSort: %d milissegundos\n", tmili);
        
        // Medir o tempo do BubbleSort
        gettimeofday(&tempo_inicial, NULL);
        bubbleSort(vetorBubbleSort, n);
        gettimeofday(&tempo_final, NULL);
        tmili = (int) (1000 * (tempo_final.tv_sec - tempo_inicial.tv_sec) + (tempo_final.tv_usec - tempo_inicial.tv_usec) / 1000);
        printf("Tempo BubbleSort: %d milissegundos\n", tmili);
        
        // Limpar a memória
        delete[] vetorQuickSort;
        delete[] vetorBubbleSort;
    }

    return 0;
}
