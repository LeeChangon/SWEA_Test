t = int(input())
for i in range(1, t+1):
    print("#", i, sep = "", end = " ")
    print(round(sum(list(map(int, input().split()))) / 10))