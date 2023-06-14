link : https://codeforces.com/contest/1779/problem/B
Code :
  t = int(input())

  while t > 0:

      a = int(input())

      if a % 2 == 0:
          print("YES")
          for i in range(0,a // 2):
              print(-1,end=' ')
              print(1,end=' ')
          print()
      else:
          if a == 3:
              print("NO")
          else:
              print("YES")
              for i in range(1,a+1):
                  if i % 2:
                      print(-(a//2 - 1),end=' ')
                  else:
                      print(a//2,end=' ')
              print()
      t -= 1
