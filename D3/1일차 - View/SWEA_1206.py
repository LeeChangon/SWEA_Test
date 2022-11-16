for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(2, n - 2):
        if arr[i] > max(max(arr[i-2:i]), max(arr[i+1:i+3])):
            cnt += arr[i] - max(max(arr[i-2:i]), max(arr[i+1:i+3]))
    print("#", tc, sep="", end=" ")
    print(cnt)
