import sys
sys.stdin = open('input.txt', 'r')
res= []
n = int(input())

for i in range(1, n+1):
    res.append(i)

print(sum(res))