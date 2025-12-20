def reverse_num(number):
    n = number
    reverse_num = 0

    while n > 0:
        last_digit = n % 10
        reverse_num = (reverse_num * 10) + last_digit
        n  = n//10


    return reverse_num

if __name__ == "__main__":
    ans = reverse_num(1234)
    print(ans)

    """
    Time Complexity - O(n)
    Space Complexity -O(n)
    """

