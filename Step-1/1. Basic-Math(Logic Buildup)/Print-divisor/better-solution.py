from typing import List

"""
Better Solution
Time Complexity -> O(N/2)

Space Complexity -> O(K) 
where k is the amount of factors
"""

class Solution:
    def printFactors(self, num: int) -> List[int]:
        result = []
        n = num
        for i in range(1, n//2+1):
            if n % i == 0:
                result.append(i)

        result.append(n)
        return result

obj = Solution()

if __name__ == "__main__":
    num = int(input("Enter Any Number : "))
    ans = obj.printFactors(num)
    print(ans)