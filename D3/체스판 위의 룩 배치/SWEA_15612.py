T = int(input())

for test_case in range(1, T + 1):
    chess = []
    chk = [0, 0, 0, 0, 0, 0, 0, 0]                                  #���� �ִ� ���� üũ�ϴ� ����Ʈ
    result = "yes"
    for _ in range(8):
        arr = input()
        if arr.count("O") == 1 and chk[arr.find("O")] == 0:         #��� ���� ���� �ϳ��� ���� ��
            chk[arr.find("O")] = 1                                 #���� �ִ� ���� üũ
        else:
            result = "no"
    print("#", test_case, sep = "", end = " ")
    print(result)
    
"""

1
......O.
.......O
...O....
O.......
....O...
..O.....
.O......
.....O..
"""