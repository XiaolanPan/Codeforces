link : https://codeforces.com/contest/1467/problem/A
Code :
t = eval(input())
while t > 0:
    v = '989'
    s = '0123456789'
    a = int(input())
    if a <= 3:
        print(v[:a])
    else:
        # s = v + s
        cnt = 1
        l = len(s)
        c = l
        while l <= a:
            cnt += 1
            l += c
        print((v + s*cnt)[:a])
    t -= 1
    
