N = int(input())
arr =[list(map(int, input().split())) for i in range(N)]

#0으로 초기화된 5x5 배열 만들기!!!


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

i = 1
j = 1

cnt = []
for i in range(N):
    for j in range(N): # 배열 A의 모든 원소에 대해서 탐색을 시작함.

        for k in range(4): # k번째 방향을 탐색함.
            ni = i + di[k]
            nj = j + dj[k]
            if ni>=0 and ni<N and nj>=0 and nj<N:
                abs_arr = abs(arr[i][j] - arr[ni][nj])
                cnt.append(abs_arr)
                res = sum(cnt)

print(res)