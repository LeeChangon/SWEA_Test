for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    
    for _ in range(n):
        arr.sort()          #배열을 오름차순으로 정렬해 가장 작은 값을 앞에
        arr[0] += 1         #가장 큰 값을 뒤에 오게 만들어
        arr[-1] -= 1        #맨 앞의 원소에 1을 더하고 맨 뒤의 원소에 1을 빼 평탄	 작업을 한다.

    arr.sort()
    result = arr[-1] - arr[0]
        
    print("#", tc, sep = "", end = " ")
    print(result)
    