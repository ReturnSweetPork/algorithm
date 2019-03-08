import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    customer = [0] * 61
    res = 0
    for i in range(M):
        t, c = map(int, input().split())
        customer[t] = -c
    # print(customer)

    for i in range(1,61):
        customer[i] = customer[i-1] + N + customer[i]
        if customer[i] <0:
            res = 1
            # break
    if res == 1:
        print(-1)
    else:
        print(customer[-1])

