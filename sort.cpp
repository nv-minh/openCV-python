// Binary Search in C++

#include <iostream>
using namespace std;
void swap(int &xp, int &yp)
{
    int temp = xp;
    xp = yp;
    yp = temp;
}
void insert(int arr[], int n)
{
    int i, key, j;  
    for (i = 1; i < n; i++) 
    {  cout<< "\n";
        key = arr[i];  
        j = i - 1;  
  
        /* Move elements of arr[0..i-1], that are  
        greater than key, to one position ahead  
        of their current position */
        while (j >= 0 && arr[j] > key) 
        {  
            arr[j + 1] = arr[j];  
            j = j - 1;  
        }  
        arr[j + 1] = key;
         for(int i=0;i<10;i++) cout << arr[i] <<"\t";  
    }  

    }

int main(void) {
  int array[] = {71, 96, 70, 55, 56, 79, 72, 64, 25, 24};
  insert(array, 10);
}