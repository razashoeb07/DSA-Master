def merge_array(left,right):
    result = []
    n = len(left)
    m = len(right)
    i,j = 0,0

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left[i])
            i += 1

    if j < m:
        while j < m:
            result.append(right[j])
            j += 1

    return result

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums)//2
    left_nums = nums[:mid]
    right_nums = nums[mid:]
    left = merge_sort(left_nums)
    right = merge_sort(right_nums)
    return merge_array(left,right)

nums = [3,2,8,5,1,4,23]
ans = merge_sort(nums)
print(ans)