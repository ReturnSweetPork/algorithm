import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    print("#", end="")
    print(tc,  end=" ")
    print(round(sum(arr)/len(arr)))