from algorithms.sort import (
    BubbleSort,
    MergeSort
)

import unittest
import sys

class TestSort(unittest.TestCase):
    """Test cases for sorting algorithms"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.merge_sort = MergeSort()
        self.bubble_sort = BubbleSort()
        
        # Define test cases
        self.test_cases = [
            ([], []),  # Empty array
            ([1], [1]),  # Single element
            ([1, 1, 1], [1, 1, 1]),  # Duplicate elements
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
            ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),  # Random order
            ([-5, 0, 10, -3, 7], [-5, -3, 0, 7, 10]),  # Negative numbers
            ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Larger array
        ]
        
    def test_merge_sort(self):
        """Test merge sort algorithm"""
        for input_arr, expected in self.test_cases:
            with self.subTest(input_arr=input_arr):
                result = self.merge_sort.sort(input_arr)
                self.assertEqual(result, expected)
                # Ensure original array wasn't modified
                if input_arr:  # Skip empty array
                    if input_arr != expected:  # Skip already sorted arrays
                        self.assertNotEqual(input_arr, result)
    
    def test_bubble_sort(self):
        """Test bubble sort algorithm"""
        for input_arr, expected in self.test_cases:
            with self.subTest(input_arr=input_arr):
                result = self.bubble_sort.sort(input_arr)
                self.assertEqual(result, expected)
                # Ensure original array wasn't modified
                if input_arr:  # Skip empty array
                    if input_arr != expected:  # Skip already sorted arrays
                        self.assertNotEqual(input_arr, result)
    
    def test_algorithm_correctness(self):
        """Test that both algorithms produce the same results"""
        for input_arr, _ in self.test_cases:
            with self.subTest(input_arr=input_arr):
                merge_result = self.merge_sort.sort(input_arr)
                bubble_result = self.bubble_sort.sort(input_arr)
                self.assertEqual(merge_result, bubble_result)

if __name__ == '__main__':
    unittest.main()