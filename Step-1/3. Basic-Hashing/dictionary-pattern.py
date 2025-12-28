"""
Example 1:
Input: arr[] = [10,5,10,15,10,5];
Output:
10  3
5   2
15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array
"""

"""
Time Complexity - O(2n) ≈ O(n)
Space Complexity - O(n)
"""
def dictionary_pattern(nums):
    n = len(nums)
    freq_dict = {}
    for i in range(n):
        if nums[i] not in freq_dict:
            freq_dict[nums[i]] = 1

        else:
            freq_dict[nums[i]] += 1

    return freq_dict

if __name__ == "__main__":
    nums = [10, 5, 10, 15, 10, 5]
    ans = dictionary_pattern(nums)

    for key, value in ans.items():
        print(key, value)