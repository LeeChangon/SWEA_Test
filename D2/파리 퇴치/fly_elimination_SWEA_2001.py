T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly = []
    mx = 0
    for i in range(N):
        fly.append(list(map(int, input().split())))
    for i in range(N - (M - 1)):
        for j in range(N - (M - 1)):
            dead = 0
            for x in range(M):
                for y in range(M):
                    dead += fly[i + x][j + y]   #범위 만큼 파리를 잡는다
             
            if(mx < dead):
                mx = dead               #최대로 잡힌 파리 수
             
    print("#", tc, sep = "", end = " ")
    print(mx)
