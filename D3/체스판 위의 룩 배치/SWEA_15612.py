T = int(input())

for test_case in range(1, T + 1):
    chess = []
    chk = [0, 0, 0, 0, 0, 0, 0, 0]                                  #룩이 있는 열을 체크하는 리스트
    result = "yes"
    for _ in range(8):
        arr = input()
        if arr.count("O") == 1 and chk[arr.find("O")] == 0:         #행과 열에 룩이 하나만 있을 때
            chk[arr.find("O")] = 1                                 #룩이 있는 열에 체크
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