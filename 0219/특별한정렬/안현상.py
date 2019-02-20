import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    leng = len(arr)
    mylist = []

    for i in range(leng):
        for j in range(i+1, leng):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


    if leng %2 == 0:
        for i in range(leng//2):
            mylist.append(arr[i])
            mylist.append(arr[leng -1 -i])

    else:
        for i in range(leng // 2):
            mylist.append(arr[i])
            mylist.append(arr[leng - 1 - i])
        mylist.append(leng//2)


    print(f"#{tc}", end=' ')
    for i in range(10):
        print(mylist[i], end=' ')
    print()


