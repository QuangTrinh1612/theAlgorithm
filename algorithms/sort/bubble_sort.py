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
        pass