#include<iostream>

using namespace std;
 void Heapify(int a[], int n, int i){
     while(i <= (n/2 -1)){
         int left = 2*i + 1;
         int right = 2*i +2;
         int max = left;
         if(right < n && a[right] > a[max]){
             max = right;
         }
         if(a[i] > a[max]){
             int temp = a[i];
             a[i] = a[max];
             a[max] = temp;
         }
         i = max;
     }
         for(int i=0; i<10; i++){
        cout << a[i] << "\t";
        }
    cout << "\n";
    
 }
void BuildHeap(int a[], int n){
    for(int i=n/2 -1; i>=0;i--){
        int temp = a[0];
        a[0] = a[i];
        a[i] = temp;
        Heapify(a, n, i);    
    }
}
void HeapSort(int a[], int n){
    BuildHeap(a, n);
    for(int i = n-1; i>=0; i--){
        int temp = a[0];
        a[0] = a[i];
        a[i] = temp; 
        Heapify(a, i, 0);
}
}
int main(){

	int arr[] = {75,66,86,73,63,91,65,80,78,24};
    HeapSort(arr, 10);
	for(int i=0; i<10; i++){
        cout << arr[i] << "\t";
    }
	return 0;
}