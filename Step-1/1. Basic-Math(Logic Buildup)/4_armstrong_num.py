from typing import Any

class Solution:
    def ArmstrongChecker(self, n: int) -> int:
        num = n
        count = 0
        armstrong = 0

        while num > 0:
            count += 1
            num = num //10

        num = n
        while num > 0:
            last_digit = num % 10
            armstrong += (last_digit ** count)
            num = num // 10

        if n == armstrong:
            return True
        else:
            return False

if __name__ == "__main__":
    obj = Solution()
    ans = obj.ArmstrongChecker(153)
    print(ans)