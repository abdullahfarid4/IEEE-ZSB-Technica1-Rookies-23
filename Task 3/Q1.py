def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
        for j in range(len(arr)):
            if (i + j) == (len(arr) - 1):
                sum2 += arr[i][j]
    sum3 = sum1 - sum2
    return abs(sum3)


n = int(input().strip())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)
