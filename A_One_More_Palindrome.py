
t = int(input())
for _ in range(t):
  s = input()
  n = len(s)
  half = n // 2
  
  new = s[:half]
  if len(set(new)) > 1:
    print("YES")
  else:
    print("NO")
       
  
