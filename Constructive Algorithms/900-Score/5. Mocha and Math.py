link : https://codeforces.com/problemset/problem/1559/A
Code :
t = eval(input())

while t > 0:
    a = int(input())
    b = list(map(int,input().split()))
    c = b[0]
    
    for i in range(1,len(b)):
        c = c & b[i]
    print(c)
    
    t -= 1
