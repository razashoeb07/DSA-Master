"""
Example 1:
Input: X = 5
Output: 120
Explanation: 5! = 5*4*3*2*1
"""

# # Functional way
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))