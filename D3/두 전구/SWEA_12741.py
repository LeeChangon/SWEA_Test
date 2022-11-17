T = int(input())
arr = []

for _ in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    n = list(range(A, B))
    m = list(range(C, D))

    cnt = min(B, D) - max(A, C)
    cnt = cnt if cnt > 0 else 0         #cnt가 0보다 작으면 0
    arr.append(cnt)

for i in range(len(arr)):
    print("#", i + 1, sep="", end=" ")
    print(arr[i])
