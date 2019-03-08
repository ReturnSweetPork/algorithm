import sys
sys.stdin = open('input.txt', 'r')
room = (input())
arr = [0] * 10
for i in range(len(room)):
    idx = int(room[i])
    arr[idx] +=1
cnt = int((arr[6] + arr[9])/2+0.5)
arr[6] = cnt
arr[9] = cnt
maxv = max(arr)



print(maxv)
