"""
Problem Statement: You are given an array. The task is to reverse the array and print it.

Examples
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

"""
def revArray(nums, start, end):
    if start > end:
        return nums

    nums[start], nums[end] = nums[end], nums[start]
    return revArray(nums, start + 1, end - 1)

if __name__ == "__main__":
    nums = [1, 2, 3]
    ans = revArray(nums, 0, len(nums) - 1)
    print(ans)