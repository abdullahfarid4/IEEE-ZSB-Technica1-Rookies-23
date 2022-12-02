x = int(input())
lst = list(map(int, input().rstrip().split()))
flag = True

while x >= 1:
    if lst[x - 1] >= 9:
        flag = False
        lst[x - 1] = 0
        lst[x - 2] += 1
        if lst[0] > 9:
            lst[0] = 0
            lst.insert(0, 1)
    elif flag:
        lst[x - 1] += 1
        break
    x -= 1

print(lst)
