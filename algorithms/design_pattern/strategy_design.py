from typing import Union, List
from algorithms.sort import BubbleSort, MergeSort, BaseSort

class SortedList:
    def __init__(self):
        self.items = []

    def set_sort_strategy(self, sort_strategy: BaseSort):
        self.strategy = sort_strategy

    def add(self, item: Union[int, str]):
        self.items.append(item)

    def sort(self):
        self.items = self.strategy.sort(self.items)