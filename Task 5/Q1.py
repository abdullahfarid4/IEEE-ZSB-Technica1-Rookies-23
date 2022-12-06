def Build_Heap(lst):
    n = (len(lst) - 1) // 2
    for i in range(n, -1, -1):
        Heap(lst, i)


def Heap(lst, i):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l < len(lst) and lst[l] > lst[i]:
        BIG = l
    else:
        BIG = i
    if r < len(lst) and lst[r] > lst[BIG]:
        BIG = r
    if BIG != i:
        temp = lst[i]
        lst[i] = lst[BIG]
        lst[BIG] = temp
        Heap(lst, BIG)


lst = [81, 13, 77, 24, 35, 61, 48, 3, 23, 87, 92, 95, 74, 57, 99, 86, 28, 15, 55, 7, 51]
Build_Heap(lst)
print(lst)
