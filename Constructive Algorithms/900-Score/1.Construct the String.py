link : https://codeforces.com/problemset/problem/1335/B
Code : 
  t = eval(input())
  s = 'abcdefghijklmnopqrstuvwxyz'
  while t > 0:
      a,b,c = map(int,input().split())
      m = s[:c]
      n = a
      a -= c
      cnt = 1
      while a >= 0:
          # m = m*2
          cnt += 1
          a -= c
      m = m * cnt
      print(m[:n])
      t -= 1
    
