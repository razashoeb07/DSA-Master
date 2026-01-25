"""
Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to
its next values, So the answer is True.
"""

def isArraySorted(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[j] < nums[i]:
                return False

    return True

if  __name__ == "__main__":
    nums = [1,2,3,4]
    ans = isArraySorted(nums)
    print(ans)

"""
Time Complexity - O(N^2)
Space Complexity - O(1)
"""