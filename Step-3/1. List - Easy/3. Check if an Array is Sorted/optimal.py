def isArraySorted(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            return False

    return True

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    ans = isArraySorted(nums)
    print(ans)

"""
Time Complexity - O(N)
Space Complexity - O(1)
"""