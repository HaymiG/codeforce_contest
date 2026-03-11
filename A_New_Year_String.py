t = int(input())
for i in range(t):
  n = int(input())
  s = input()
  count = 0 
  if s.__contains__("2026"):
    count = 0
  elif s.__contains__("2025") :
    count += 1
  print(count)

    
    