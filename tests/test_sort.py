from algorithms.sort import (
    BubbleSort,
    MergeSort
)

import unittest
import sys

class SortFactory:
    """
    Factory class to create the appropriate Sort implementation.
    """
    
    @staticmethod
    def create_sorter(algorithm_name):
        """
        Create a sorter based on the algorithm name.
        
        Args:
            algorithm_name: String name of the algorithm (e.g., 'bubble', 'merge')
            
        Returns:
            Sort: An instance of a concrete Sort implementation
            
        Raises:
            ValueError: If the algorithm name is not recognized
        """
        if algorithm_name.lower() == 'bubble':
            return BubbleSort()
        elif algorithm_name.lower() == 'merge':
            return MergeSort()
        else:
            raise ValueError(f"Unknown sorting algorithm: {algorithm_name}")

class TestSort(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        algorithm = self.algorithm_name if hasattr(self, 'algorithm_name') else 'bubble'
        self.sorter = SortFactory.create_sorter(algorithm)
        print(f"Testing with {self.sorter.__class__.__name__}")
        
    def test_empty_array(self):
        """Test sorting an empty array"""
        arr = []
        result = self.sorter.sort(arr)
        self.assertEqual(result, [])
        self.assertTrue(self.sorter.is_sorted(result))
        
    def test_sorted_array(self):
        """Test sorting an already sorted array"""
        arr = [1, 2, 3, 4, 5]
        result = self.sorter.sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertTrue(self.sorter.is_sorted(result))
        
    def test_reverse_sorted_array(self):
        """Test sorting a reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        result = self.sorter.sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertTrue(self.sorter.is_sorted(result))
        
    def test_random_array(self):
        """Test sorting a random array"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = self.sorter.sort(arr)
        self.assertEqual(result, sorted(arr))
        self.assertTrue(self.sorter.is_sorted(result))
        
    def test_array_with_duplicates(self):
        """Test sorting an array with duplicate elements"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = self.sorter.sort(arr)
        self.assertEqual(result, sorted(arr))
        self.assertTrue(self.sorter.is_sorted(result))
        
    def test_array_with_negative_numbers(self):
        """Test sorting an array with negative numbers"""
        arr = [3, -1, 4, -1, 5, -9, 2, 6, -5]
        result = self.sorter.sort(arr)
        self.assertEqual(result, sorted(arr))
        self.assertTrue(self.sorter.is_sorted(result))
        
    def test_original_array_unchanged(self):
        """Test that the original array remains unchanged"""
        arr = [5, 4, 3, 2, 1]
        original = arr.copy()
        self.sorter.sort(arr)
        self.assertEqual(arr, original)
        
if __name__ == '__main__':

    # Process command line arguments
    if len(sys.argv) > 1 and sys.argv[1] in ['bubble', 'merge']:
        # Store the algorithm name and remove it from sys.argv
        # so that unittest.main() doesn't try to process it
        TestSort.algorithm_name = sys.argv[1]
        sys.argv.pop(1)
    else:
        # Default to bubble sort if no algorithm is specified
        TestSort.algorithm_name = 'bubble'
        print("No valid algorithm specified. Using bubble sort by default.")
        print("Usage: python test_sort.py [bubble|merge]")
    
    unittest.main()