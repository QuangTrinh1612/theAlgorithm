from algorithms.sort import BaseSort

class SelectionSort(BaseSort):
    def sort(self, arr):
        n = len(arr)
        
        for i in range(n-1):
            min_id = i
            
            for j in range(i+1,n):
                if arr[j] < arr[min_id]:
                    min_id = j
            
            arr[i], arr[min_id] = arr[min_id], arr[i]
        
        return arr

if __name__ == '__main__':
    unsorted_array = [64,25,12,22,11]
    print(SelectionSort().sort(unsorted_array))