lst = list(map(int, input().split()))
minny = 9999999

for i in range(len(lst)):
    if lst.count(lst[i]) < 2:
        continue
    else:
        for j in range(i+1, len(lst)):
            k = abs(j - i)
            if ( lst[i] == lst[j] ) and ( k < minny ):
                minny = abs(j - i)

print(minny)
