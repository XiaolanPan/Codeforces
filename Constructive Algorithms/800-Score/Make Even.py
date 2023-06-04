t = eval(input())

while t > 0:
    v = input()
    # print(v[-1])
    if int(v[-1]) % 2 == 0:
        print(0)
        # continue
    elif int(v[0]) % 2 == 0:
        print(1)
    else:
        flag = False
        
        for i in v:
            a = int(i)
            if a % 2 == 0:
                flag = True
                break
            
        
        if flag:
            print(2)
        else:
            print(-1)
    
    t -= 1
    
