for _ in range(10):
    n = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    mx = 0
    
    print("#", n, sep = "", end = " ")
    cr1 = 0
    cr2 = 0
    cnt1 = 0
    cnt2 = 4
    varr = [0] * 100
    for i in range(100):            #세로줄 합
        for j in range(100):          
            varr[i] += arr[j][i]
    
    for i in arr:                
        cr1 += i[cnt1]              #대각선 합
        cnt1 += 1
        cr2 += i[cnt2]
        cnt2 -= 1
        
        if sum(i) > mx:             #가로줄 합
            mx = sum(i)

    if max(cr1, cr2, max(varr)) > mx:
        mx = max(cr1, cr2, max(varr))
    print(mx)
