"""
Print numbers from 1 to N
"""

# Without backtracking
def func1(i, n):
    if n < i:
        return

    print(i)
    func1(i+1, n)

# With backtracking
def func2(i, n):
    if i < 1:
        return
    func2(i - 1, n)
    print(i)


if __name__ == "__main__":
    func1(1,5) # Without backtracking

    func2(5,5) # With backtracking