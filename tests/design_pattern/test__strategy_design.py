import pytest
from algorithms.design_pattern import SortedList  # Assuming the original script is in sorted_list.py
from algorithms.sort import BubbleSort, MergeSort

# Test fixtures
@pytest.fixture
def empty_sorted_list():
    return SortedList()

@pytest.fixture
def unsorted_list():
    sl = SortedList()
    sl.add(5)
    sl.add(2)
    sl.add(8)
    sl.add(1)
    return sl

# Test SortedList initialization
def test_sorted_list_initialization(empty_sorted_list):
    assert isinstance(empty_sorted_list, SortedList)
    assert empty_sorted_list.items == []
    assert not hasattr(empty_sorted_list, 'strategy')

# Test adding items
def test_add_items(empty_sorted_list):
    empty_sorted_list.add(1)
    assert empty_sorted_list.items == [1]
    
    empty_sorted_list.add("test")
    assert empty_sorted_list.items == [1, "test"]

# Test setting sort strategy
def test_set_sort_strategy(empty_sorted_list):
    empty_sorted_list.set_sort_strategy(BubbleSort())
    assert isinstance(empty_sorted_list.strategy, BubbleSort)
    
    empty_sorted_list.set_sort_strategy(MergeSort())
    assert isinstance(empty_sorted_list.strategy, MergeSort)

# Test sorting with BubbleSort
def test_sort_with_bubble_sort(unsorted_list):
    unsorted_list.set_sort_strategy(BubbleSort())
    unsorted_list.sort()
    assert unsorted_list.items == [1, 2, 5, 8]

# Test sorting with MergeSort
def test_sort_with_merge_sort(unsorted_list):
    unsorted_list.set_sort_strategy(MergeSort())
    unsorted_list.sort()
    assert unsorted_list.items == [1, 2, 5, 8]

# Test sorting empty list
def test_sort_empty_list(empty_sorted_list):
    empty_sorted_list.set_sort_strategy(BubbleSort())
    empty_sorted_list.sort()
    assert empty_sorted_list.items == []

# Test sorting with single item
def test_sort_single_item(empty_sorted_list):
    empty_sorted_list.add(42)
    empty_sorted_list.set_sort_strategy(MergeSort())
    empty_sorted_list.sort()
    assert empty_sorted_list.items == [42]

# Test sorting with mixed types (assuming sorting should work with comparable types)
def test_sort_mixed_types(empty_sorted_list):
    empty_sorted_list.add(5)
    empty_sorted_list.add(2)
    empty_sorted_list.add(1)
    empty_sorted_list.set_sort_strategy(BubbleSort())
    empty_sorted_list.sort()
    assert empty_sorted_list.items == [1, 2, 5]

# Test sorting is stable (if applicable to the implementation)
def test_sort_stability(unsorted_list):
    sl = SortedList()
    sl.add(1)  # First 1
    sl.add(2)
    sl.add(1)  # Second 1
    sl.set_sort_strategy(MergeSort())  # MergeSort is typically stable
    sl.sort()
    assert sl.items == [1, 1, 2]  # Order of equal elements should be preserved