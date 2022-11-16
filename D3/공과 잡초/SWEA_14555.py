T = int(input())

for tc in range(1, T + 1):
    n = input()
    result = 0
    result += n.count("()") + n.count("(|") + n.count("|)")

    print("#", tc, sep="", end=" ")
    print(result)
