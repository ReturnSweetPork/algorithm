import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N 은 수강생 K는 과제낸사람
    arr = list(map(int, input().split()))
    mylist = []
    for i in range(1, N+1):
        mylist.append(i)

    for j in range(K):
        mylist.remove(arr[j])

    print(f"#{tc}", end=" ")
    for k in range(len(mylist)):
        print(mylist[k], end=" ")
    print()



