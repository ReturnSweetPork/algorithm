import sys
sys.stdin = open('input.txt', 'r')
mylist = [0,0,0,0,0,0,0,0,0,0,0,0]
ans = 0
m = 0 # 부분집합의 숫자 갯수들이잖아
n = 0 # 부분집합의 합이자나
def group(idx, cnt):
    global mylist, m, n, ans # 잘 모르겟지만 위에 숫자를 함수 안에서도 쓰게 해주는 함수
    if m == cnt:
        group_sum = 0
        for i in range(0,12):
            if mylist[i] ==1:
                group_sum += i+1
        #         print(i+1,end=' ')
        # print()
        if group_sum == n:
            ans +=1
        return

    for j in range(idx,12):
        mylist[j] = 1
        group(j+1, cnt+1)
        mylist[j] = 0

T = int(input())
for tc in range(T):
    m,n = map(int, input().split())
    cnt = 0
    ans = 0
    mylist = [0,0,0,0,0,0,0,0,0,0,0,0]
    group(0,0)
    print(f"#{tc+1} {ans}")




