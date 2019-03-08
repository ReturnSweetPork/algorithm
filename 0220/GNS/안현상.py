import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T +1):
    N, M = input().split()
    arr = list(map(str, input().split()))
    org_list=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    mylist=[]
    for i in range(10):
        for j in range(int(M)):
            if org_list[i] == arr[j]:
                mylist.append(org_list[i])
    print(N)
    for i in range(len(mylist)):
        print(mylist[i], end=" ")


