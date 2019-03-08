import sys
sys.stdin = open('input.txt', 'r')

def safe(x,y):
    return x>=0 and y>=0 and x<N and y<N

def bfs(x,y):
    global visited, arr
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = []
    q. append((x,y))
    visited[x][y] = 1
    cnt = 1
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if safe(nx, ny) and visited[nx][ny] ==0 and arr[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt +=1
    return cnt


N = int(input())
arr = [list(map(int, input())) for x in range(N)]
visited = [[0]*N for i in range(N)]
res = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            res.append(bfs(i,j))
print(res)
