import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    res = int(n/m)
    cnt = n%m

    print("#{} {} {}".format(tc, res, cnt))