import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    length_A, length_B = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res_list = []
    maxV = 0
    max_list = []
    print("#", end="")
    print(tc, end=" ")
    if len(A) == len(B):
        for i in range(len(A)):
            maxV += A[i]*B[i]
    elif len(A) > len(B):
        for k in range(len(A) - len(B)+1):
            for j in range(len(B)):
                max_list.append(A[j+k] * B[j])
            res_list.append(sum(max_list))
            max_list = []
        print(max(res_list))
    elif len(A) < len(B):
        for k in range(len(B) - len(A)+1):
            for j in range(len(A)):
                max_list.append(A[j] * B[j+k])
            res_list.append(sum(max_list))
            max_list = []
        print(max(res_list))







