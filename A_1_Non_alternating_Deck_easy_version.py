t = int(input())
for _ in range(t):
    n = int(input())
    a = b = 0
    i = 1 

    while n > 0:
        cur = min(i, n)
        if i == 1:
            a += cur
        elif ((i - 2) // 2) % 2 == 0:
            b += cur
        else:
            a += cur

        n -= cur
        i += 1

    print(a, b)