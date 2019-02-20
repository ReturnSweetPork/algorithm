import sys
sys.stdin = open('input.txt', 'r')

T = 10
N = 100

for tc in range(1, 11):
    num = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    sum_colum = 0
    sum_row = 0
    sum_cross = 0
    sum_cross_reverse = 0
    res = []
    for i in range(100):
        for j in range(100):
            sum_colum += arr[i][j]
            res.append(sum_colum)
            sum_row += arr[j][i]
            res.append(sum_row)
        sum_colum = 0
        sum_row = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum_cross += arr[i][j]
                res.append(sum_cross)

            elif 100-i == 100-j:
                sum_cross_reverse += arr[i][j]
                res.append(sum_cross_reverse)
        sum_cross = 0
        sum_cross_reverse = 0

    print(f"#{tc} {max(res)}")


