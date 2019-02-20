import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = 0
sum_list = []
for tc in range(1, T+1):

    for i in range(n-m+1):
        for j in range(m):
            arr_sum = arr_sum + (arr[i+j])
        sum_list.append(arr_sum)
        arr_sum = 0
    res = max(sum_list) - min(sum_list)

    print(f"#{tc} {res}")