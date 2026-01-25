def second_small_large(nums):
    n = len(nums)
    smallest = nums[0]
    s_smallest = float("inf")
    largest = nums[0]
    s_largest = float("-inf")

    for i in range(n):
        if nums[i] <= smallest:
            smallest = nums[i]

        if nums[i] >= largest:
            largest = nums[i]

    for i in range(n):
        if nums[i] > smallest and nums[i] < s_smallest:
            s_smallest = nums[i]

        if nums[i] < largest and nums[i] > s_largest:
            s_largest = nums[i]

    return s_smallest,s_largest

if __name__ == "__main__":
    nums = [2, 5, 1, 3, 0]
    ans = second_small_large(nums)
    print(ans)