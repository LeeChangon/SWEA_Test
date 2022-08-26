from collections import deque

for i in range(10):
    tc = int(input())
    pw = deque(list(map(int, input().split())))
    
    cnt = 1
    while pw[-1] != 0:              #맨 뒤 숫자가 0이 되면 완성
        a = pw.popleft() - cnt
        if cnt == 5:
            cnt = 0
        cnt += 1
        
        if a < 0:
            a = 0
        pw.append(a)
        
    print("#", tc, sep = "", end = " ")
    print(*pw)

"""
1
10 6 12 8 9 4 1 3
"""