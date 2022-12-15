def kClosest(points: list[list[int]], k: int):
    lst = []
    lst2 = []
    for i in points:
        res = i[0] ** 2 + i[1] ** 2
        lst.append(res)
    while k > 0:
        k -= 1
        m1 = min(lst)
        m = lst.index(m1)
        lst2.append(points[m])
        points.remove(points[m])
        lst.remove(min(lst))
    return lst2
