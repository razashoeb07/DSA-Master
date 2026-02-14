"""
Input:
nums = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]
Explanation:
Initially, nums = [1, 2, 3, 4, 5]
Rotating once to the left results in nums = [2, 3, 4, 5, 1].
"""

def leftRotateByOne(nums):
    temp = nums.pop(0)
    nums.append(temp)

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    leftRotateByOne(nums)
    print(nums)

"""
Time Complexity - O(N) because all remaining elements must shift left.
Space Complexity - O(1)
"""
