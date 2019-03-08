import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    fly = []
    res = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = []
            for k in range(M):
                for l in range(M):
                    fly.append(arr[i+k][j+l])

            res.append(sum(fly))
    print("#", end="")
    print(tc, end=" ")
    print(max(res))
