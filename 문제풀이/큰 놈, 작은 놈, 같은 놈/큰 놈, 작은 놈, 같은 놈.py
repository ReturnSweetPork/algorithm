import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    print("#", end="")
    print(tc, end=" ")
    if N > M:
        print(">")
    elif N < M:
        print("<")
    elif N == M:
        print("=")