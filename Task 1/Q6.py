m = int(input())
n = int(input())
small = 0
if m > n:
    small = n
else:
    small = m
for i in range(2, small):
    if (m % i == 0) & (n % i == 0):
        small = i
print(small)