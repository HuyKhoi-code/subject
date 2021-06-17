def count_money(n):
  count = 0
  a = []
  for i in range(n//500000+1):
    for j in range(n//200000+1):
      for k in range(n//100000+1):
        for m in range(n//50000+1):
          alpha = n-(i*500000+j*200000+k*100000+m*50000)
          if (alpha % 20000 == 0) and alpha>=0: 
            count +=1
            a.append(i+j+k+m+int(alpha/20000))
  return count,a[-1]
n = int(input())
x,y = count_money(n)
print(x, y)