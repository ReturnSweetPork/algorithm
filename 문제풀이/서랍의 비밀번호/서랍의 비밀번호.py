import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
res = []
for i in range(m, 999):
    res.append(i)
    if i == n:
        print(res.index(i)+1)