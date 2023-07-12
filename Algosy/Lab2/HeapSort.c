#include <stdio.h>
#include <math.h>

//https://www.codegrepper.com/code-examples/cpp/heapify+c

void swap(int *a, int *b){
    
    int temp = *a;
    *a = *b;
    *b = temp;

}

void heapify(int arr[], int n, int i){
    int largest = i; 
    int l = 2 * i + 1;
    int r = 2 * i + 2;
 
    
    if (l < n && arr[l] > arr[largest])
        largest = l;
 
    
    if (r < n && arr[r] > arr[largest])
        largest = r;
 
    
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}
 
void heapSort(int arr[], int n){

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
 

    for (int i = n - 1; i > 0; i--) {
       
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}
 

void printArray(int arr[], int n){
    for (int i = 0; i < n; ++i){
        printf("%d, ",arr[i]);
    }
}

int main(){
    FILE *HBS, *HAS; //HBS = HeapBeforeSort HAS = HeapAfterSort

    HBS = fopen("C:\\Users\\filip\\Desktop\\VSC\\Algosy\\Lab2\\HeapBeforeSort.txt","r");
    HAS = fopen("C:\\Users\\filip\\Desktop\\VSC\\Algosy\\Lab2\\HeapAfterSort.txt","w");

    printf("To which index would you like to HeapSort your array?: ");
    int x;
    scanf("%d",&x);
    int arr[6];

    for(int i=0;i<sizeof(arr) / sizeof(arr[0]);i++){
        fscanf(HBS,"%d",&arr[i]);
    }
    
    heapSort(arr, x);
    // printf("Sorted Array to index %d : \n",x);
    // printArray(arr,x);
    printf("Sorted Array to index %d : \n",x);
    printArray(arr,sizeof(arr) / sizeof(arr[0]));

    for(int i=0;i<sizeof(arr) / sizeof(arr[0]);i++){
        fprintf(HAS,"%d\n",arr[i]);
    }

    fclose(HBS);
    fclose(HAS);
    
    return 0;
}

