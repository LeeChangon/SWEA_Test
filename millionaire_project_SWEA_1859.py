T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    b = list(map(int, input().split()))
    
    profit = 0
    max_v = b[-1]
    for i in range(N-1, -1, -1):    #������ �� ���� �������� ����Ѵ�
        if max_v <= b[i]:           #�ִ밪 ���� Ŭ �� ������ �����ش�.
            max_v = b[i]
        profit += max_v - b[i]
    print("#", tc, " ", profit, sep = "")