import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    num = []
    num2 = []
    for i in range(N-M+1):
        for j in range(M):
            num.append(arr[i+j])
        res = sum(num)
        num = []
        num2.append(res)
    print("#", end='')
    print(tc, end=' ')
    print(max(num2)-min(num2))