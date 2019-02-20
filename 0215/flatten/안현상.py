import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    maxidx = 0
    minidx = 0
    for d in range(dump):
        for i in range(100):
            if box[maxidx] < box[i]:
                maxidx = i
            if box[minidx] > box[i]:
                minidx = i

        box[maxidx] -= 1
        box[minidx] += 1


#체크만 하고 끝나니까 한번 더 돌려줌 !!

    for j in range(100):
        if box[maxidx] < box[j]:
            maxidx = j
        if box[minidx] > box[j]:
            minidx = j

    res = box[maxidx] - box[minidx]

    print(f"#{tc} {res}")

