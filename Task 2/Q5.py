def insertion_sort(lst : list):
    for i in range(1, len(lst)):
        x = lst[i]
        y = i - 1
        while (y > -1) & (lst[y] > x):
            lst[y + 1] = lst[y]
            y -= 1
        lst[y + 1] = x
    return lst

l = [6, 4, 3, 7, 6, 6, 5, 1, 3, 9, 0]
print(insertion_sort(l))