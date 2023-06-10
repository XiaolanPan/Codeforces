link : https://codeforces.com/contest/1401/problem/A
Code : 
  t = eval(input())

  while t > 0:

      a,b = map(int,input().split())
      if a <= b:
          print(b - a)
      else:
          m = (a + b) // 2
          print(abs((m - a) - (b - m)))
      t -= 1
    
