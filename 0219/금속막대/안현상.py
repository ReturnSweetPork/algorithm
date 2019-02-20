
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    mylist = []
    res = []
    length = len(arr)
    for i in range(1, len(arr), 2):
        mylist.append(arr[i])

    for j in range(0, len(arr), 2):
        if arr[j] not in mylist:
            res.append(arr[j])
            res.append(arr[j + 1])
            del arr[j]
            del arr[j]
            break

    while len(res) != length:
        for k in range(0, len(arr), 2):
            if res[-1] == arr[k]:
                res.append(arr[k])
                res.append(arr[k + 1])

                break

    print(f"#{tc}", end=" ")
    for l in res:
        print(l, end=' ')
    print()