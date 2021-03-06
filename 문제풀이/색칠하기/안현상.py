import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr_red = [[0]*10 for i in range(10)]
    arr_blue = [[0] * 10 for i in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1:
            for x in range(r1, r2 +1):
                for y in range(c1, c2 +1):
                    arr_red[x][y] = 1

        else:
            for x in range(r1, r2 +1):
                for y in range(c1, c2 +1):
                    arr_blue[x][y] = 1

    cnt = 0
    for x in range(10):
        for y in range(10):
            if arr_red[x][y] == 1 and arr_blue[x][y] == 1:
                cnt += 1
    print("#", end='')
    print(tc, end=' ')
    print(cnt)
