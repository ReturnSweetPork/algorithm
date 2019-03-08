import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    res = []
    arr_sort = sorted(arr)
    for i in range(N//2):
        res.append(arr_sort[(N-i)-1])
        res.append(arr_sort[i])

    print("#", end="")
    print(tc, end=" ")
    for j in range(10):
        print(res[j], end=" ")
    print()