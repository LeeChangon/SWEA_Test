T = int(input())

az = "abcdefghijklmnopqrstuvwxyz"
for tc in range(1, T + 1):
    n = input()
    cnt = 0

    for i in n:
        if i == az[cnt]:
            cnt += 1
        else:
            break
    print("#", tc, sep = "", end = " ")
    print(cnt)
