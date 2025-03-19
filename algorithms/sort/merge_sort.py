from algorithms.sort import BaseSort

class MergeSort(BaseSort):
    def sort(self, arr):
        """
        Sort the given array using bubble sort algorithm.
        
        Args:
            arr: List of comparable elements to be sorted
            
        Returns:
            List: Sorted list of elements
        """

        result = arr
        n = len(result)

        for i in range(n):
            
            swap = False

            for j in range(n-i-1):
                if result[j] > result[j+1]:
                    result[j], result[j+1] = result[j+1], result[j]
                    swap = True
            
            if not swap:
                break
        
        return result
