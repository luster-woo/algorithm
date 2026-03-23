import sys
input = sys.stdin.readline
from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y]=cnt
    while q:
        x,y = q.popleft()
        for i in range(4):
            ni = x+dx[i]
            nj = y+dy[i]
            if 0<=ni<n and 0<=nj<n and l<=abs(maze[ni][nj]-maze[x][y])<=h and visited[ni][nj]==-1:
                visited[ni][nj]=cnt
                q.append((ni,nj))
                graph[cnt].append((ni,nj))
n,l,h = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
day = 0

while True:
    cnt = 0
    graph = [[] for _ in range(n*n+1)]
    visited = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==-1:
                graph[cnt].append((i,j))
                bfs(i,j)
                cnt+=1

    for idx in graph:
        result = 0
        temp = 0 
        for x,y in idx:
            result+=maze[x][y]
            temp+=1
        if idx:
            result //= len(idx)
            for x,y in idx:
                maze[x][y]=result
    if cnt ==n*n:
        break
    day +=1

print(day)