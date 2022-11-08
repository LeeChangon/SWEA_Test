from itertools import combinations
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    
    for i in range(1, N + 1):
        parr = list(combinations(arr, i))
        for j in parr:            
            if sum(j) == K:                      #합이 K라면
                result += 1
    print("#", test_case, sep = "", end = " ")
    print(result)