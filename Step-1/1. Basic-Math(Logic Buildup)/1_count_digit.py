def count_digit(number):
    n = number
    count = 0
    while n > 0:
        count += 1
        n = n//10
    return count

if __name__ == "__main__":
    ans = count_digit(12345)
    print(ans)

    """
    Time Complexity - O(n)
    space complexity - O(1)
    """