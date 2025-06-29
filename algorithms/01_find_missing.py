def solution_naive(A):
    """
    Naive approach: Check each positive integer starting from 1
    Time Complexity: O(n²) in worst case
    Space Complexity: O(1)
    """
    current = 1
    while True:
        if current not in A:
            return current
        current += 1

def solution_sorting(A):
    """
    Sorting approach: Sort array and find the gap
    Time Complexity: O(n log n)
    Space Complexity: O(1) if in-place sorting
    """
    A_sorted = sorted([x for x in A if x > 0])  # Filter positive numbers and sort
    
    if not A_sorted or A_sorted[0] > 1:
        return 1
    
    expected = 1
    for num in A_sorted:
        if num == expected:
            expected += 1
        elif num > expected:
            return expected
    
    return expected

def solution_set(A):
    """
    Set approach: Use set for O(1) lookups
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    positive_nums = set(x for x in A if x > 0)
    
    current = 1
    while current in positive_nums:
        current += 1
    
    return current

def solution_optimal(A):
    """
    Optimal approach: Use array indices as hash map
    Time Complexity: O(n)
    Space Complexity: O(1) - modifies input array in-place
    
    Key insight: The answer must be in range [1, n+1] where n is array length
    """
    n = len(A)
    
    # Step 1: Replace all numbers <= 0 or > n with a placeholder (n+1)
    for i in range(n):
        if A[i] <= 0 or A[i] > n:
            A[i] = n + 1
    
    # Step 2: Use indices as hash map - mark presence by making values negative
    for i in range(n):
        num = abs(A[i])
        if num <= n:
            # Mark that number 'num' is present by making A[num-1] negative
            if A[num - 1] > 0:
                A[num - 1] = -A[num - 1]
    
    # Step 3: Find first positive number - its index+1 is the missing number
    for i in range(n):
        if A[i] > 0:
            return i + 1
    
    # If all numbers 1 to n are present, return n+1
    return n + 1

def solution_optimal_no_modify(A):
    """
    Optimal approach without modifying input
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(A)
    present = [False] * (n + 1)  # present[i] represents if number i is in array
    
    # Mark which numbers from 1 to n are present
    for num in A:
        if 1 <= num <= n:
            present[num] = True
    
    # Find first missing number
    for i in range(1, n + 1):
        if not present[i]:
            return i
    
    return n + 1

# Test functions
def test_solutions():
    """Test all solutions with provided examples"""
    test_cases = [
        ([1, 3, 6, 4, 1, 2], 5),
        ([1, 2, 3], 4),
        ([-1, -3], 1),
        ([1], 2),
        ([2, 3, 4], 1),
        ([1, 2, 3, 4, 5], 6),
        ([], 1),
        ([-5, -10, 0], 1),
        ([1000000], 1)
    ]
    
    solutions = [
        ("Naive", solution_naive),
        ("Sorting", solution_sorting),
        ("Set", solution_set),
        ("Optimal (modifies input)", solution_optimal),
        ("Optimal (no modify)", solution_optimal_no_modify)
    ]
    
    print("Testing all solutions:\n")
    
    for i, (arr, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: A = {arr}, Expected = {expected}")
        
        for name, func in solutions:
            # Create copy for functions that might modify input
            test_arr = arr.copy()
            try:
                result = func(test_arr)
                status = "✓" if result == expected else "✗"
                print(f"  {name:25}: {result} {status}")
            except Exception as e:
                print(f"  {name:25}: Error - {e}")
        print()

if __name__ == "__main__":
    test_solutions()

# Performance comparison
import time
import random

def benchmark_solutions():
    """Benchmark different solutions with various input sizes"""
    print("\nPerformance Benchmark:")
    print("=" * 50)
    
    sizes = [100, 1000, 10000, 50000]
    solutions = [
        ("Set", solution_set),
        ("Sorting", solution_sorting),
        ("Optimal (modifies)", solution_optimal),
        ("Optimal (no modify)", solution_optimal_no_modify)
    ]
    
    for size in sizes:
        print(f"\nArray size: {size}")
        print("-" * 30)
        
        # Create test data: mix of positive, negative, and missing numbers
        test_data = (
            list(range(1, size//2)) +  # Some consecutive positive numbers
            [-random.randint(1, 1000) for _ in range(size//4)] +  # Negative numbers
            [random.randint(size, size*2) for _ in range(size//4)]  # Large positive numbers
        )
        random.shuffle(test_data)
        
        for name, func in solutions:
            test_arr = test_data.copy()
            
            start_time = time.time()
            result = func(test_arr)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"{name:20}: {execution_time:8.3f} ms (result: {result})")

# Uncomment to run benchmark
benchmark_solutions()