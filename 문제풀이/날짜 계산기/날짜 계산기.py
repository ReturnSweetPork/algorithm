import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = list(map(int, input().split()))
    d = d2 - d1
    m = m2 - m1
    M = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # print(m)
    # print(d)
    month = 0
    print("#", end="")
    print(tc, end=" ")
    if m ==0:
        print(d+1)
    else:
        for i in range(m):
            month += M[i+m1]
        res = month + d2 - d1 +1
        print(res)