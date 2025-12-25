"""
Complexity Analysis
Time Complexity: O(N), we print every number from N to 1 using recursion
Space Complexity: O(N), stack space used for recursive calls.
"""

# Forward Recursion (Without Backtracking)
def func1(i):
    if i < 1:
        return

    print(i)
    func1(i-1)


# With Backtracking
def func2(i,n):
    if i > n:
        return

    func2(i+1,n)
    print(i)


if __name__ == "__main__":
    func1(5) # Without Backtracking
    func2(1,5) # With Backtracking