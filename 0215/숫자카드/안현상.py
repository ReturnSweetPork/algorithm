import sys
sys.stdin = open('sample_input_num.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    cnt = int(input())
    num = input()
    numlist = []
    numlist_no = []
    maxV = 0
    maxC = 0
    for i in range(len(num)):
        a = int(num[i])
        numlist.append(a)
    for j in numlist:
        if j not in numlist_no:
            numlist_no.append(j)
    for n in numlist_no:
        if numlist.count(n) >= maxV and n > maxC:
            maxV = numlist.count(n)
            maxC = n
    print(f"#{tc} {maxC} {maxV}")

