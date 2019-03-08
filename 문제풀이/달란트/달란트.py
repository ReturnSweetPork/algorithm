import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, P = map(int, input().split())

    if N%P == 0:
        maxV = int(pow(N/P,P))
    else:
        maxV = pow(int(N/P), (P -N%P))*pow(int(N / P)+1, N%P)

    print("#{} {}".format(tc, maxV))

