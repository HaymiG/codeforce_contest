t = int(input())
n = list(map(int , input().split()))
expected = (t*(t + 1)) // 2
actual = sum(n)
print(expected - actual)

