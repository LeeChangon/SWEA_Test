T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    b = list(map(int, input().split()))
    
    profit = 0
    max_v = b[-1]
    for i in range(N-1, -1, -1):    #마지막 날 부터 역순으로 계산한다
        if max_v <= b[i]:           #최대값 보다 클 때 이익을 더해준다.
            max_v = b[i]
        profit += max_v - b[i]
    print("#", tc, " ", profit, sep = "")