link: https://codeforces.com/contest/1196/problem/A
Code:
  t = eval(input())

  while t > 0:

      a = sorted(list(map(int,input().split())))
      # int(7/2) 和 7 // 2 是不一样的
      print(sum(a)//2)

      t -= 1
    
