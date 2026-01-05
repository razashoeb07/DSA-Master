def greatest_common_divisor(n1,n2):
    gcd = 1
    for i in range(1, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

if __name__ == "__main__":
    n1 = 9
    n2= 12
    print(greatest_common_divisor(n1,n2))