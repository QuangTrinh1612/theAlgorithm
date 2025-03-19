from abc import ABC, abstractmethod

class BaseSort(ABC):
    """
    Abstract base class for sorting algorithms.
    """

    @abstractmethod
    def sort(self, arr):
        """
        Sort the given array using the algorithm.
        
        Args:
            arr: List of comparable elements to be sorted
            
        Returns:
            List: Sorted list of elements
        """
        pass

    def is_sorted(self, arr):
        """
        Check if an array is sorted.
        
        Args:
            arr: List of comparable elements
            
        Returns:
            bool: True if the array is sorted, False otherwise
        """
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))