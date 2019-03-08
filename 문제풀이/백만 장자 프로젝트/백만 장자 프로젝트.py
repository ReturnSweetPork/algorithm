import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    re_arr = list(reversed(arr))
    maxprice = re_arr[0]

    res = 0
    for j in range(N):
        if re_arr[j] < maxprice:
            res += maxprice - re_arr[j]
        else:
            maxprice = re_arr[j]
    print("#", end="")
    print(tc, end=" ")
    print(res)


