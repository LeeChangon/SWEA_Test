T = int(input())

for test_case in range(1, T + 1):
    print("#", i, sep = "", end = " ")
    n, m = map(int, input().split())
    if n + m >= 24:
        pirnt(n + m - 24)
    
