import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int, input().split())) + [0]
start = 0   #오르막 구간의 시작 인덱스
status = 0 #오르막 구간은 1이고 나머지는 0이다.
maxV = 0
for i in range(n): #오른쪽과 비교할 자리i
    if status == 0 and arr[i]<arr[i+1]: #오르막의 시작임!!!!
        start = i
        status = 1
    elif status ==1 and arr[i]>=arr[i+1]: #오르막이 끝난다면
        diff = arr[i] - arr[start]
        if maxV < diff: #가장 큰 오르막찾기
            maxV = diff
        status = 0 #오르막 초기화

print(maxV)

