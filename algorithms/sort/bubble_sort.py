"""

https://en.wikipedia.org/wiki/Bubble_sort

Worst-case performance: O(N^2)

If you call bubble_sort(arr,True), you can see the process of the sort
Default is simulation = False

"""

from algorithms.sort import BaseSort

class BubbleSort(BaseSort):
    """
    Concrete implementation of bubble sort algorithm.
    """

    def sort(self, arr):
        """
        Sort the given array using bubble sort algorithm.
        
        Args:
            arr: List of comparable elements to be sorted
            
        Returns:
            List: Sorted list of elements
        """
        # Create a copy to avoid modifying the original
        result = arr.copy()
        n = len(result)
        
        # Traverse through all array elements
        for i in range(n):
            # Flag to optimize if no swapping occurs
            swapped = False
            
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # Swap if current element is greater than next
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
                    
            # If no swapping occurred in this pass, array is sorted
            if not swapped:
                break
                
        return result