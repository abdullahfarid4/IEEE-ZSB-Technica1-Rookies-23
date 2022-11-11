Sum = 0
n = int(input())
for i in range(1, n+1):
    if (i % 5 == 0) | (i % 3 == 0):
        Sum += i
print(Sum)