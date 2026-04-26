"""
Given a sorted array arr[] and a number target, the task is to find the upper bound of the target in this given array.
The upper bound of a number is defined as the smallest index in the sorted array where the element is
greater than the given number.

such that: arr[i] > x

Note: If all the elements in the given array are smaller than or equal to the target, the upper bound
will be the length of the array.

Examples :

Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
Output: 3
Explanation: 3 is the smallest index in arr[], at which element (arr[3] = 10) is larger than 9.
"""
from typing import List

def upperBound(arr: List[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    ans = n

    while low <= high:
        mid = (low + high)//2

        if arr[mid] > target:
            ans = mid
            high = mid-1

        else:
            low = mid+1

    return ans

if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 9
    result = upperBound(arr, target)
    print(result)

"""
Time Complexity: O(log n)
Space Complexity - O(1)
"""