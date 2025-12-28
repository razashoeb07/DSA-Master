def freq(nums):
    hash_map = {}

    # Pre compute frequencies
    for i in nums:
        hash_map[i] = hash_map.get(i, 0) + 1

    return hash_map


nums = [5, 4, 2, 5, 4, 2, 1, 1, 1, 3, 5, 3]

hash_map = freq(nums)   # function call with argument

number = int(input("Enter number to count = "))
print(hash_map.get(number, 0))
