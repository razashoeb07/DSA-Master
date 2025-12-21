from typing import Any

class Solution:
    def palindromeChecker(self, n: int) -> bool:
        if n < 0:
            return False  # negative numbers are not palindrome

        num = n
        palindromeCheck = 0

        while num > 0:
            last_digit = num % 10
            palindromeCheck = (palindromeCheck * 10) + last_digit
            num = num //10

        if n == palindromeCheck:
            return True
        else:
            return False

if __name__ == "__main__":
    obj = Solution()
    ans = obj.palindromeChecker(121)
    print(ans)
