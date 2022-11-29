lst = []
list2 = []

L = input().split()
n = int(L[0])
m = int(L[1])
c = list(map(int, input().rstrip().split()))

for i in range(n):
    for j in range(len(c)):
        lst.append(abs(c[j] - i))
    list2.append(min(lst))
    lst = []
print(max(list2))

