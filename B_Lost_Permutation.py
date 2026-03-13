t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))

    present = set(b)
    max_val = max(present)

    current = 1
    while s > 0:
        if current not in present:
            s -= current
            present.add(current)
            if current > max_val:
                max_val = current
        current += 1
   
    if s == 0:
        ok = True
        for x in range(1, max_val + 1):
            if x not in present:
                ok = False
                break
        print("YES" if ok else "NO")
    else:
        print("NO")
