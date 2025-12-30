"""
Example 1:
Input: N = 5, array[] = [5,4,3,2,1]
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5
"""

"""
Bubble sort
Time complexity - O(n^2) (Average and worst)
Time complexity - O(n) (Best case) - if the array is already sorted! 
Space complexity - O(1)
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
        swap = False
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swap = True
        if swap == False:
            break

    return nums

if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    ans = bubble_sort(nums)
    print(ans)