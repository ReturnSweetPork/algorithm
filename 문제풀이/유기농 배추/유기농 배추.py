import sys
sys.stdin = open('input.txt','r')

def search(i,j,M,N):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]


    q = []
    q.append(i)
    q.append(j)
    visited[i][j] = 1
    while len(q) != 0: #큐가 비어있지 않는다면
        i = q.pop(0)
        j = q.pop(0)
        #arr[i][j] = 0 #vistited를 사용하지 않는경우
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if ni>=0 and ni<n and nj>=0 and nj<m:
                if arr[ni][nj] == 1 and visited[ni][nj] ==0: #지우는경우 if arr[ni][nj] == 1만 사용
                    q.append(ni)
                    q.append(nj)
                    visited[ni][nj] =1











T = int(input())
for tc in range(1,T+1):
    M, N, K = map(int,input().split())
    arr = [[0]*M for i in range(M)]
    visited = [[0]*M for i in range(M)]
    for i in range(K):
        c, r = arr(int, input().split())
        arr[r][c] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j]==0:
                cnt += 1
                search(i,j,M,N)
    print(cnt)

# def bfs(x,y):
#     q = []#큐생성
#     #visited main에서 생성한다.
#     #시작점 인큐
#     #시작점에 방문표시 visited[i][j] = 1 또는 map[i][j] = 0
#     while len(q) = 0:#q가 비어있지 않으면 반복
#         q.pop(0)#i와 j를 디큐를 실행
#         map[i][j] = 0
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if ~~
#