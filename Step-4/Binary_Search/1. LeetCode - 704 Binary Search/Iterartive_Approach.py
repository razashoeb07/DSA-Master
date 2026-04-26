"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    n = len(nums)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return -1

if __name__  == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = search(nums,9)
    print(result)