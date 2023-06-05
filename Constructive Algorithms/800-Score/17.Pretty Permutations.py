link: https://codeforces.com/problemset/problem/1541/A
Code:
  
  t = eval(input())

  while t > 0:
      l = eval(input())

      if l % 2 == 0:
          pos = 2
          while pos <= l:
              print(pos,pos - 1,end=' ')
              pos += 2
      else:
          af = l - 3
          pos = 2
          while pos <= af:
              print(pos,pos - 1,end=' ')
              pos += 2

          print(l - 1,l,l - 2,end=' ')
      print()
      t -= 1
    
