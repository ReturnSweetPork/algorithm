# import sys
# sys.stdin = open('sample_input.txt', 'r')
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr_max = 0
#     arr_min = 1000000
#     for i in range(1, len(arr)):
#         if arr[i] > arr_max:
#             arr_max = arr[i]
#         if arr[i] < arr_min:
#             arr_min = arr[i]
#     print(f"#{tc} {arr_max - arr_min}")


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    print(arr)

