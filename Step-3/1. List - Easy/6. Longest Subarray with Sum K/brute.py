def longestSubarray(nums,k):
    n = len(nums)
    max_len = 0

    for i in range(n):
        current_sum = 0
        for j in range(i,n):
            current_sum += nums[j]

            if current_sum == k:
                max_len = max(max_len, j-i+1)

    return max_len

if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, -10]
    k = 15
    ans = longestSubarray(nums,k)
    print(ans)

"""
Time Complexity = O(n^2)
Space Complexity - O(1) 
"""
