"""
Example 1:
Input:
 N = 6, array[] = {9, -3, 3, -1, 6, -5}
Result:
 5
Explanation:
 The following subarrays sum to zero:
{-3, 3}
{-1, 6, -5}
{-3, 3, -1, 6, -5}
The length of the longest subarray with sum zero is 5.
"""

def longestSubarray(nums):
    n = len(nums)
    max_len = 0

    for i in range(n):
        total = 0
        for j in range(i,n):
            total += nums[j]

            if total == 0:
                max_len = max(max_len, j-i+1)

    return max_len

if __name__ == "__main__":
    nums = [9, -3, 3, -1, 6, -5]
    ans = longestSubarray(nums)
    print(ans)


"""
Time Complexity - O(N^2)
Space Complexity - O(1)
"""