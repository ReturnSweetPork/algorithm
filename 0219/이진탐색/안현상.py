import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1,T+1):
    P, A, B = map(int, input().split())
    cnt_a = 0
    cnt_b = 0

    left = 1
    right = P
    while True:
        mid = (left+right)//2
        cnt_a += 1
        if A == mid:
            break
        elif A > mid:
            left = mid
        else:
            right = mid

    left = 1
    right = P
    while True:
        mid = (left+right)//2
        cnt_b += 1
        if B == mid:
            break
        elif B > mid:
            left = mid
        else:
            right = mid

    if cnt_a == cnt_b:
        print(f"#{tc} 0")
    elif cnt_a < cnt_b:
        print(f"#{tc} A")
    else:
        print(f"#{tc} B")
