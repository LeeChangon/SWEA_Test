for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    
    for _ in range(n):
        arr.sort()          #�迭�� ������������ ������ ���� ���� ���� �տ�
        arr[0] += 1         #���� ū ���� �ڿ� ���� �����
        arr[-1] -= 1        #�� ���� ���ҿ� 1�� ���ϰ� �� ���� ���ҿ� 1�� �� ��ź	 �۾��� �Ѵ�.

    arr.sort()
    result = arr[-1] - arr[0]
        
    print("#", tc, sep = "", end = " ")
    print(result)
    