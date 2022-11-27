s = 'hello'
ss = input()
i = 0
j = 0
while i < len(s) and j < len(ss):
    if s[i] == ss[j]:
        i += 1
    j += 1
if i == len(s):
    print("YES")
else:
    print("NO")