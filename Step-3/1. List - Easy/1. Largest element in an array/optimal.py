def largestElement(nums):
    if not nums:
        return None

    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest


if __name__ == "__main__":
    nums = [10, 52, 98, 75, 25, 452]
    print(largestElement(nums))
