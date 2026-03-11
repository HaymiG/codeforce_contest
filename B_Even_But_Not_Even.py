
t = int(input())
for _ in range(t):
  n = input()
  s = input()
  answer = ""
  for char in s:
    if int(char) % 2 != 0:
      answer += char
      if len(answer) == 2:
        break
  if len(answer) == 2:
    print(answer)
  else:
    print("-1")
    


      
      

    
