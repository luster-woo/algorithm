from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
num = int(input())
for seq in range(1,num+1):
    n,m = map(int,input().split())
    visited=[[-1]*m for _ in range(n)]
    maze = [list(input().strip()) for _ in range(n)]
    water = deque()
    for x in range(n):
        for y in range(m):
            if maze[x][y]=="W":
                water.append((x,y))
                visited[x][y]=0
    while water:
        x,y = water.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1 and maze[nx][ny]=="L":
                visited[nx][ny]=visited[x][y]+1
                water.append((nx,ny))
    result = 0
    for x in range(n):
        for y in range(m):
            if visited[x][y]!=0:
                result+=visited[x][y]
    print(f'#{seq} {result}')