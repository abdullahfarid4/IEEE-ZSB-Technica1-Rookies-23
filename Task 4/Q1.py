n, k = map(int, input().split())
lst = list(map(int, input().split()))

temp = []
freq = []
lst2 = list(set(lst))

for i in lst2:
    x = lst.count(i)
    freq.append(x)

res = dict(zip(freq, lst2))

for i in sorted(res, reverse=True):
    temp.append(res[i])

print(temp[:k])
