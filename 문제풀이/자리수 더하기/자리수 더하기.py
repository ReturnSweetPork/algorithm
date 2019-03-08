import sys
sys.stdin = open('input.txt', 'r')

N = str(input())
res = []
for i in range(len(N)):
    res.append(int(N[i]))

print(sum(res))
