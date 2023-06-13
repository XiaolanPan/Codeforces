link : https://codeforces.com/contest/1525/problem/B
Code :
  t = eval(input())

  while t > 0:

      a = int(input())

      b = list(map(int,input().split()))

      is_sort = True

      for i in range(0,a):
          if b[i] != (i + 1):
              is_sort = False
              break
      if is_sort:
          print(0)
      elif b[0] == 1 or b[a - 1] == a:
          print(1)
      elif b[0] == a and b[a - 1] == 1:
          print(3)
      else:
          print(2)

      t -= 1
