import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    cnt_a = 0
    cnt_b = 0


    left = 1
    right = P
    while True:
        mid = int((left+right)/2)
        if A == mid:
            break
        elif A > mid:
            left = mid
            cnt_a +=1
        else:
            right = mid
            cnt_a +=1

    left = 1
    right = P
    while True:
        mid = int((left+right)/2)
        if B == mid:
            break
        elif B > mid:
            left = mid
            cnt_b +=1
        else:
            right = mid
            cnt_b +=1


    print("#", end = "")
    print(tc, end = " ")
    if cnt_a > cnt_b:
        print("B")
    elif cnt_a < cnt_b:
        print("A")
    elif cnt_a == cnt_b:
        print(0)

