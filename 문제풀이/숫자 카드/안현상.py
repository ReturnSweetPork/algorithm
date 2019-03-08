import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    numlist = []
    numlist_no = []
    N = int(input())
    num = input()
    for i in range(N):
        numlist.append(num[i])


    for j in numlist:
        if j not in numlist_no:
            numlist_no.append(j)
    maxc= 0
    maxv = 0
    for k in numlist_no:
        v = int(k)
        if numlist.count(k) > maxc and v > maxv:
            maxc = numlist.count(k)
            maxv = v

    print("#", end="")
    print(tc, end=" ")
    print(maxv, end=" ")
    print(maxc)