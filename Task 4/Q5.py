def rotate(lst, n):
    lst_big = []
    for i in range(n):
        lst_temp = []
        for j in range(n-1, -1, -1):
            lst_temp.append(lst[j][i])
        lst_big.append(lst_temp)
    return lst_big


ls = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
lst2 = rotate(ls, 3)
print(lst2)
