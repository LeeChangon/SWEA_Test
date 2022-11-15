T = int(input())

for tc in range(1, T + 1):
    n = input()
    print("#", tc, sep="", end=" ")
    if n.count("o") + (15 - len(n)) >= 8:
        print("YES")
    else:
        print("NO")
