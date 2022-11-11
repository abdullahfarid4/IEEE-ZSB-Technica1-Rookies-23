m = int(input())
m2 = str(m)
m = m2[::-1]
print(int(m))
if m == m2:
    print("YES")
else:
    print("NO")
