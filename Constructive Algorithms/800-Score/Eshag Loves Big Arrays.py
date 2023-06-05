link:https://codeforces.com/contest/1529/problem/A
Code:
  t = eval(input())

  while t > 0:
      l = eval(input())
      a = sorted(list(map(int,input().split())))
      # print(a)

      s = 1
      for i in range(1,l):
          if a[i] != a[i - 1]:
              # s += 1
              break
          s += 1
      if s == l:
          print(0)
      else:
          print(l - s)

      # break
      t -= 1
    
