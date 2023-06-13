link : https://codeforces.com/contest/768/problem/A
Code : 
  n = eval(input())

  v = list(map(int,input().split()))

  ma,mi = max(v),min(v)

  cnt = 0

  for i in v:
      if i > mi and i < ma:
          cnt += 1
  print(cnt)
