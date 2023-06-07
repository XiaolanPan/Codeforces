link : https://codeforces.com/problemset/problem/1400/A
Code : 
  t = eval(input())

  while t > 0:

      n = int(input())

      s = input()

      if n == 1:
          print(s,end='')
      else:
          for i in range(0,len(s)):
              if i % 2 == 0:
                  print(s[i],end='')
      print()
      t -= 1
    
