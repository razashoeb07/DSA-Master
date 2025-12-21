from typing import List

"""
Brute Solution
Time Complexity -> O(N)

Space Complexity -> O(K) 
where k is the amount of factors
"""

class Solution:
    def printFactors(self, num: int) -> List[int]:
        result = []
        n = num
        for i in range(1, n+1):
            if n % i == 0:
                result.append(i)

        return result

obj = Solution()

if __name__ == "__main__":
    num = int(input("Enter Any Number : "))
    ans = obj.printFactors(num)
    print(ans)