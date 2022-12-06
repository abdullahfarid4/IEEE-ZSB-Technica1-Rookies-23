def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


x = int(input())
y = x // 2
lst = []
for i in range(1, y+1):
    if isPrime(i):
        lst.append(i)
i = 0
while i < len(lst):
    if x == 1:
        break
    if x % lst[i] == 0:
        x /= lst[i]
        print(lst[i], end=' ')
        i = 0
    else:
        i += 1
