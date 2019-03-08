import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

for i in range(1, 10000):
    if n%i == 0:
        print(i, end=" ")