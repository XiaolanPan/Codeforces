link: https://codeforces.com/contest/1702/problem/A
code:
t = eval(input())

while t > 0:
    v = input()
    
    n = int(v)
    leng = len(v)
    # print(leng)
    
    # print(10**(leng-1))
    
    print(n - 10**(leng-1))
    
    t -= 1
    
