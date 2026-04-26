from typing import List

def binary_search(nums:List[int], low: int, high: int, target: int) -> int:
    if low > high:
        return -1

    mid = (low + high)//2
    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        return binary_search(nums, mid+1, high, target)

    else:
        return binary_search(nums, low, mid-1, target)

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    n = len(nums)
    result = binary_search(nums,0,n-1,target)
    print(result)

"""
Time Complexity - O(log n)
Space Complexity - O(log n)

Note - Recursion uses multiple call stack frames, while iteration reuses the same variables in a single 
        frame.
"""