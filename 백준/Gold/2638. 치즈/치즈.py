import sys
input = sys.stdin.readline
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    visited[x][y]=1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        visited[x][y]=1
        for i in range(4):
            di = x+dx[i]
            dj = y+dy[i]
            if 0<=di<n and 0<=dj<m and visited[di][dj]==0 and maze[di][dj]==0:
                visited[di][dj]=1
                q.append((di,dj))
def delete():
    while cheeze:
        x,y = cheeze.popleft()
        cnt = 0
        for i in range(4):
            di = x+dx[i]
            dj = y+dy[i]
            if 0<=di<n and 0<=dj<m and maze[di][dj] == 0 and visited[di][dj] == 1:
                cnt+=1
        if cnt>=2:
            maze[x][y]=0

n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
flag = False
while True:
    cheeze = deque()
    visited = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if maze[x][y]==1:
                cheeze.append((x,y))
            if (x==0 or y==0 or x==n-1 or y==m-1) and visited[x][y]==0 and maze[x][y]==0:
                bfs(x,y)
    delete()
    cnt +=1
    if not any(1 in row for row in maze):
        break
print(cnt)
