def missingNum(arr):
    n = len(arr) + 1

    # Calculate the sum of array elements
    totalSum = sum(arr)
    print(totalSum)
    # Calculate the expected sum
    expSum = n * (n + 1) // 2
    print(expSum)

    # Return the missing number
    return expSum - totalSum

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))