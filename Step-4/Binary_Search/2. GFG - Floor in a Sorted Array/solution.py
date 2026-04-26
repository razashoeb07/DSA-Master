"""
Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[]
that is less than or equal to x. This element is called the floor of x. If such an element does not exist,
return -1.

such that = arr[i] <= x

Note: In case of multiple occurrences of floor of x, return the index of the last occurrence.
"""

from typing import List

def floor(arr: List[int], x: int):
    n = len(arr)
    ans = -1
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] <= x:
            ans = mid
            low = mid+1

        else:
            high = mid-1

    return ans

if __name__ == "__main__":
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    result = floor(arr, x)
    print(result)