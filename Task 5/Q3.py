x = int(input())
lst = []

while True:
    x = sum(int(i) ** 2 for i in str(x))
    if x == 1 or x in lst:
        break
    else:
        lst.append(x)

if x == 1:
    print("true")
else:
    print("false")
