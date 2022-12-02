lst = []


def perm(string, start, end):
    if start == end:
        x = ''.join(string)
        lst.append(x)
    else:
        for i in range(start, end):
            string[start], string[i] = string[i], string[start]
            perm(string, start + 1, end)
            string[start], string[i] = string[i], string[start]
    return lst


str1 = list(input())
str2 = input()
ls = perm(str1, 0, len(str1))
for i in ls:
    if i in str2:
        print(True)
        break
else:
    print(False)
