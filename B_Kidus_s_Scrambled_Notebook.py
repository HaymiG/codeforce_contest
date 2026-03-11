t = int(input())
for i in range(t):
  s = input()
  found = False 

  for j in range(1,len(s)):
      a = s[:j]
      b = s[j:]
      if a[0] == "0" or b[0] == "0":
         continue    
      A = int(a)
      B = int(b)
      if A > 0 and B > 0 and B > A:
         print (A ,B)
         found = True
         break
  if not found:
         print("-1")
         
   





  
