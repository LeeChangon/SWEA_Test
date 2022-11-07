#T = int(input())

for test_case in range(1, 11):
    T = int(input())
    astr = input()
    bstr = input()
    print("#", T, sep = "", end = " ")
    print(bstr.count(astr))