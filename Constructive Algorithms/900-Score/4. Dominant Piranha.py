link : https://codeforces.com/problemset/problem/1433/C
Code :
t = eval(input())

while t > 0:
    a = int(input())
    b = list(map(int,input().split()))
    
    ma = b.index(max(b)) + 1
    cnt = 0
    value = max(b)
    
    for v in b:
        if v == value:
            cnt += 1
    
    if cnt == a:
        print(-1)
    else:
        flag = False
        
        for i in range(1,a):
            if b[i] == value or b[i - 1] == value:
                if b[i] != b[i - 1]:
                    if b[i] > b[i - 1]:
                        print(i + 1)
                    else:
                        print(i - 1 + 1)
                    flag = True
                    break
    t -= 1
    
