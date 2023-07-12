#include <stdio.h> //https://www.geeksforgeeks.org/quick-sort/

#define c 0

void swap(int* a, int* b) { 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 


void bubbleSort(int arr[], int low, int high){

    for(int i = low; i < high - 1; i++){
        for(int j = 0; j < high - i - 1; j++){
            if(arr[j] > arr[j+1]){
                swap(&arr[j], &arr[j+1]);
            }
        }
    }

}

int partition (int arr[], int low, int high) { 
    int pivot = arr[high]; 
    int i = (low - 1); 
  
    for (int j = low; j <= high - 1; j++) { 
        
        if (arr[j] <= pivot) { 
            i++; 
            swap(&arr[i], &arr[j]); 
        } 
    } 
    swap(&arr[i + 1], &arr[high]); 
    return (i + 1); 
} 

void quickSort(int arr[], int low, int high) { 
    if (low + c < high){ 
        
        int pi = partition(arr, low, high); 
  
       
        quickSort(arr, low, pi - 1); 
        quickSort(arr, pi + 1, high); 
    } 
    else{
        bubbleSort(arr,low,high);
    }
} 

void printArray(int arr[], int size) {  
    for (int i = 0; i < size; i++){ 
         printf("%d, ",arr[i]); 
    }

} 


int main(){
    int arr[] = {10, 7, 8, 9, 1, 5}; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    quickSort(arr, 0, n - 1); 
    printf("Sorted Array: \n"); 
    printArray(arr, n); 
    
    return 0;
}

