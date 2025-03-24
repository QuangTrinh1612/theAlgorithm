import pytest
from algorithms.sort import BubbleSort, MergeSort

@pytest.fixture
def sorting_algorithms():
    return {
        "merge_sort": MergeSort(),
        "bubble_sort": BubbleSort()
    }

@pytest.mark.parametrize("input_arr, expected", [
    ([], []),
    ([1], [1]),
    ([1, 1, 1], [1, 1, 1]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
    ([-5, 0, 10, -3, 7], [-5, -3, 0, 7, 10]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
])
def test_sorting_algorithms(sorting_algorithms, input_arr, expected):
    for name, sorter in sorting_algorithms.items():
        result = sorter.sort(input_arr)
        assert result == expected, f"{name} failed for input {input_arr}"
        
        # Ensure original array wasn't modified
        if input_arr and input_arr != expected:
            assert input_arr != result, f"{name} modified the original input {input_arr}"

@pytest.mark.parametrize("input_arr", [
    [], [1], [1, 1, 1], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5],
    [3, 1, 4, 1, 5, 9, 2, 6], [-5, 0, 10, -3, 7], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
])
def test_algorithm_correctness(sorting_algorithms, input_arr):
    merge_result = sorting_algorithms["merge_sort"].sort(input_arr)
    bubble_result = sorting_algorithms["bubble_sort"].sort(input_arr)
    assert merge_result == bubble_result, f"Sorting algorithms produced different results for input {input_arr}"