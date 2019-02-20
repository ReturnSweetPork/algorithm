import sys
sys.stdin = open('sample_input_bus.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr_busstop = list(map(int, input().split()))
    # print(arr[1])# 종점인 정류장 번호   갯수로는 1개를 더 추가해야함
    # print(arr[0])# 최대 이동 가능 정류장 수
    # print((arr[1]+1)/arr[0])
    max_chai = 0
    for i in range(len(arr_busstop)-1):
        # print(arr_busstop[i-1])
        if arr_busstop[i] < arr_busstop[i+1]:
            chai = arr_busstop[i+1] - arr_busstop[i]
            if chai > max_chai:
                max_chai = chai
    # print(max_chai)
    # print(arr[0])
    cnt = 0

    if arr[0] < max_chai:
        # print(0)
        print(f"#{tc} 0")
    else:
        bus = arr_busstop[0]
        for j in range(len(arr_busstop)-1):
            # print(j)
            # print(arr[0]*j)
            # print(arr_busstop[j])
            if bus < arr[0]:

                bus = arr_busstop[j] + arr[0]
                cnt = cnt + 1
                print(cnt)
            # print(arr_busstop[j+1])
            # print(arr[0]*(j+1))
        #     if arr_busstop[j] <= arr[0]*(j+1) <= arr_busstop[j+1] <= arr[1]:
        #         cnt+= 1
        # print(cnt)


    #
    # print(arr_busstop_max - arr_busstop_min)
