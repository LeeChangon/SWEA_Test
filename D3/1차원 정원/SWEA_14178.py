T = int(input())

for tc in range(1, T + 1):
    n, d = map(int, input().split())
    d = d * 2 + 1                 #양쪽으로 분무되는 분무기
    result = n // d
    if n % d != 0:
        result += 1
    print("#", tc, sep="", end=" ")
    print(result)
