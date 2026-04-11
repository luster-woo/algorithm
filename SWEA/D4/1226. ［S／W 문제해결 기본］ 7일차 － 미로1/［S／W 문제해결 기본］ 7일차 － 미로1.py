from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for _ in range(10):
    n = int(input())
    print(f'#{n} ',end="")
    maze = [list(map(int,input().strip())) for _ in range(16)]
    visited= [[0]*16 for _ in range(16)]
    sx,sy=0,0
    ex,ey=0,0
    for x in range(16):
        for y in range(16):
            if maze[x][y]==2:
                sx,sy=x,y
            elif maze[x][y]==3:
                ex,ey=x,y
    q = deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    result = 0
    while q:
        x,y=q.popleft()
        if x==ex and y==ey:
            result =1
            break
        for i in range(4):
            ni = x+dx[i]
            nj = y+dy[i]
            if 0<=ni<16 and 0<=nj<16 and visited[ni][nj]==0 and maze[ni][nj]!=1:
                q.append((ni,nj))
                visited[ni][nj]=1
    print(result)