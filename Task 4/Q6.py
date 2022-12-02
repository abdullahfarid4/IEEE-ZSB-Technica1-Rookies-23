res1 = input()
flag = 0

while res1 != '6174':
    y = int("".join(sorted(res1)))
    z = int("".join(sorted(res1, reverse=True)))
    res = z - y
    if len(str(res)) < 4:
        res1 = '0'*(4 - len(str(res))) + str(res)
    else:
        res1 = str(res)
    flag += 1

print(flag)
