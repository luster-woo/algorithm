from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def island_cnt(x,y,cnt):
    q = deque()
    q.append((x,y))
    visited[x][y]=1
    maze[x][y]=cnt
    while q:
        x,y = q.popleft()
        for i in range(4):
            ni = x + dx[i]
            nj = y + dy[i]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0 and maze[ni][nj]==1:
                visited[ni][nj]=1
                maze[ni][nj]=cnt
                q.append((ni,nj))

n = int(input())
maze = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
temp = 1
for x in range(n):
    for y in range(n):
        if maze[x][y]==1 and visited[x][y]==0:
            island_cnt(x,y,temp)
            temp+=1
dist = [[-1]*n for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(n):
        if maze[i][j] > 0:
            q.append((i,j))
            dist[i][j] = 0
ans = 10**9
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if maze[nx][ny] == 0:
                maze[nx][ny] = maze[x][y]
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
            elif maze[nx][ny] != maze[x][y]:
                ans = min(ans, dist[nx][ny] + dist[x][y])            
print(ans)