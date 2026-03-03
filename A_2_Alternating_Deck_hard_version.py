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
    white_a = black_a =white_b =black_b = 0 
    
  
    for i in range(1 ,a+1 , 1):
      if i % 2 != 0:
        white_a += 1
      else :
        black_a += 1
    for i in range(1 ,b+1 , 1):
      if i % 2 != 0:
        white_b += 1
      else :
        black_b += 1
    print(white_a , black_a ,  black_b ,white_b )
    