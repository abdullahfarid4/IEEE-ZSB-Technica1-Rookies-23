n = int(input())
p = int(input())

flag = 0
page1 = 1
page_n = n

while not (p == 1 or p == n):
    if p <= (n / 2):
        page1 += 2
        flag += 1
        if page1 >= p:
            break
    else:
        page_n -= 2
        flag += 1
        if page_n <= p:
            break

print(flag)
