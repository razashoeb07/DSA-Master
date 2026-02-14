def leftRotateByOne(nums):
    nums[:] = nums[1:] + nums[:1]

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    leftRotateByOne(nums)
    print(nums)

"""
Time Complexity: O(N) → slicing copies elements
Space Complexity: O(N) → new temporary list created
It appears that an in-place change is taking place, but a temporary list is being created internally.
that's why space is O(N)
"""