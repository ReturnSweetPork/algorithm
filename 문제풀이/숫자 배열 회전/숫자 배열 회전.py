import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for x in range(n)]
    arr_90 = []
    arr_180 = []
    arr_270 = []

    for x in range(n):
        for y in range(n):
            arr_90.append(arr[n-1-y][x])

    for x in range(n):
        for y in range(n):
            arr_180.append(arr[n-1-x][n-1-y])

    for x in range(n):
        for y in range(n):
            arr_270.append(arr[y][n-1-x])

    # print(arr_90)
    # print(arr_180)
    # print(arr_270)

    print("#", end="")
    print(tc, end="")
    print()
    for i in range(n):
        for x in (arr_90[i*n:(i+1)*n ]):
            print(x, end="")
        print(" ", end="")

        for x in (arr_180[i*n:(i+1)*n ]):
            print(x, end="")
        print(" ", end="")
        for x in (arr_270[i*n:(i+1)*n ]):
            print(x, end="")
        print()