def fib(n):
    if n <= 1:
        return n
    first = fib(n-1)
    last = fib(n-2)
    return  first + last


print(fib(7))