import os


def circularArrayRotation(a, k, queries):
    lst = []
    temp = a[len(a) - 1]
    x = len(a) % k
    while x > 0:
        a.remove(temp)
        a.insert(0, temp)
        x -= 1
        temp = a[len(a) - 1]

    for i in queries:
        lst.append(a[i])

    return lst


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
