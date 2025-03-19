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

        # Base case
        if len(arr) <= 1:
            return arr
            
        # Divide array into two halves
        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        
        # Merge the sorted halves
        return self.__merge(left, right)

    def __merge(self, left, right):
        """Merge two sorted arrays"""
        result = []
        i = j = 0
        
        # Compare elements from both arrays and add smaller one to result
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result
