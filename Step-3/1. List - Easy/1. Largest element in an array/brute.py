"""
Input: arr[] = [2, 5, 1, 3, 0]
Output: 5
Explanation: 5 is the largest element in the array.
"""

"""
Complexity Analysis
Time Complexity: O(N log N), where N is the size of the array, as we are sorting the array.
Space Complexity: O(1), as we are using a constant
"""

def largestElement(nums):
    nums.sort()
    return nums[-1]

if __name__ == "__main__":
    nums = [10,52,98,75,25,452]
    print(largestElement(nums))