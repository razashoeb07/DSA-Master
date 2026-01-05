n1 = 9
n2 = 12
Factors_of_9 = []
Factors_of_12 = []

for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0:
        Factors_of_9.append(i)

    if n2 % i == 0:
        Factors_of_12.append(i)

left = 0
right = 0
i, j = 0, 0
result = []
while i < len(Factors_of_9) and j < len(Factors_of_12):
    if Factors_of_9[i] == Factors_of_12[j]:
        result.append(Factors_of_9[i])
        i += 1
        j += 1
    j += 1

print(result[-1])