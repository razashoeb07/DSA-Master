"""
Sum of numbers from 1 to N
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15
"""

def add(i, sum):
    if i < 1:
        print(sum)
        return

    add(i-1, sum+i)

if __name__ == "__main__":
    add(3,0)