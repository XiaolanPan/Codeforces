link : https://codeforces.com/contest/1840/problem/A
Code :
t = eval(input())

while t > 0: 
    n = int(input())
    s = input()
    r = len(s)
    ss = s[0]
    l = 0
    while l < r:
        
        for i in range(l + 1,r):
            if s[i] == s[l]:
                print(s[i],end='')
                l = i + 1
                break
    print()
    t -= 1
    
