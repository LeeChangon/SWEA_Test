T = int(input())

for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    print("#", tc, sep = "", end = " ")

    if X < L:
        print(L - X)
    elif U < X:
        print(-1)
    else:
        print(0)
