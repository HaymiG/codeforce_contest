t = int(input())
for _ in range(t):
  n = int(input())
  
  arr = list(map(int,input().split()))
  arr.sort()
  

  result = sum(arr[::2])
  print (result)
