from collections import deque
T = int(input())

dx = [0, 1, 0, -1]          #우 하 좌 상
dy = [1, 0, -1, 0]
dr = deque([0, 1, 2, 3])

for tc in range(1, T + 1):
    N = int(input())
    
    arr = [[-1] * N for _ in range(N)]
    
    x, y, n = 0, 0, 1
    arr[0][0] = 1
    
    while n < N * N:        
        nx = x + dx[dr[0]]
        ny = y + dy[dr[0]]
        print(nx, ny, n)
        
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == -1:            
            n += 1
            arr[nx][ny] = n
            x = nx
            y = ny
        else:
            dr.append(dr.popleft())     #배열 제일 앞 원소를 맨 뒤로 보냄(방향을 바꿈)
        
            
        
        
    
    print("#", tc, sep = "")
    
    for i in arr:
        for j in i:
            print(j, end = ' ')
        print()    
    