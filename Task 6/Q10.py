def friend(n, k ,lst1):
    lst2 = []
    for i in lst1:
        while k and lst2 and lst2[-1] < i:
            lst2.pop()
            k -= 1
        lst2.append(i)
    print(" ".join(map(str, lst2)))


t = int(input())
lst = []
while t > 0:
    t -= 1
    n, k = input().split()
    n = int(n)
    k = int(k)
    lst = list(map(int, input().split()))
    friend(n, k ,lst)

