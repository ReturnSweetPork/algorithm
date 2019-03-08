import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    T = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, T-2):
        if arr[i] - arr[i-1] >=2 and arr[i] - arr[i-2] >=2 and arr[i] - arr[i+1] >=2 and arr[i] - arr[i+2] >=2:
            mylist = []
            mylist.append(arr[i-1])
            mylist.append(arr[i-2])
            mylist.append(arr[i+1])
            mylist.append(arr[i+2])
            maxV = 0
            for max in mylist:
                if maxV < max:
                    maxV = max
            cnt += arr[i] - maxV

    print(f"#{tc} {cnt}")