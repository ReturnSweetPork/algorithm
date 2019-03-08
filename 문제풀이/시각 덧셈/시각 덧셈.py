import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2

    if m >= 60:
        h = h+1
        m = m-60
    if h >=13:
        h = h -12
    print("#", end="")
    print(tc, end=" ")
    print(h, end=" ")
    print(m)