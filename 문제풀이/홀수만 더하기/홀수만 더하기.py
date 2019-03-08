import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    res = []
    for i in range(10):
        if arr[i] %2 != 0:
            res.append(arr[i])

    print("#{} {}".format(tc, sum(res)))