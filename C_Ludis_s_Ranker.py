n = int(input())
a = list(map(int, input().split()))

ans = []

for i in range(n):
    higher = 0
    for j in range(n):
        if a[j] > a[i]:
            higher += 1
    ans.append(higher + 1)

print(*ans)
