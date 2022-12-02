dic = {}
n = int(input())

for i in range(n):
    ele = input()
    ele2 = "".join(sorted(ele))
    if ele2 in dic.keys():
        dic[ele2].append(ele)
    else:
        dic[ele2] = []
        dic[ele2].append(ele)

for values in dic.values():
    print(values)
