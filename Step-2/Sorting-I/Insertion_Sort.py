"""
Time Complexity: O(n^2), where n is the number of elements in the array.
This is because, in the worst case, we may have to compare each element with all the previous elements.

Space Complexity: O(1), as we are sorting the array in place and not using any
additional data structures that grow with input size.
"""

def insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1

        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j = j-1

        nums[j+1] = key

    return nums

if __name__ == "__main__":
    nums = [7,4,1,3,5]
    ans = insertion_sort(nums)
    print(ans)
