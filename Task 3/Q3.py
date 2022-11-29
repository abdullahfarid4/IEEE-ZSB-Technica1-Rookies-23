lst_rem = []
lst_cap = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    lst_rem.append(x)
    lst_cap.append(y)

total = sum(lst_rem)
cap = sum(sorted(lst_cap)[-2:])

if total > cap:
    print("No")
else:
    print("Yes")


