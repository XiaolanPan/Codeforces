link: https://codeforces.com/problemset/problem/1626/A
code:
  t = eval(input())

  while t > 0:

      s = input()

      n_dict = {}

      for i in s:
          n_dict[i] = 0

      for i in s:
          n_dict[i] += 1

      # print(n_dict)

      for i in n_dict:
          l = n_dict[i]
          print(i*l,end='')
      print()

      t -= 1
    
