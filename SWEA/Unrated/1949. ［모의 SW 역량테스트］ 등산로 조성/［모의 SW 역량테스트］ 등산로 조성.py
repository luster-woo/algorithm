dx = [0,1,0,-1]
dy = [1,0,-1,0]
def backtrack(x,y,cnt,use):
    global max_val
    max_val = max(max_val, cnt)
    for i in range(4):
        ni = x+dx[i]
        nj = y+dy[i]
        if 0<=ni<n and 0<=nj<n:
            temp = maze[x][y]-maze[ni][nj]
            if visited[ni][nj]==0 and temp>0:
                visited[ni][nj]=1
                backtrack(ni,nj,cnt+1,use)
                visited[ni][nj]=0
            elif visited[ni][nj]==0 and temp<=0 and use == 0:
                if maze[ni][nj]-k<maze[x][y]:
                    original = maze[ni][nj]
                    maze[ni][nj] = maze[x][y] - 1
                    visited[ni][nj] = 1
                    backtrack(ni, nj, cnt+1, use+1)
                    visited[ni][nj] = 0

                    maze[ni][nj] = original
num = int(input())
for seq in range(1,num+1):
    n,k = map(int,input().split())
    maze = [list(map(int,input().split())) for _ in range(n)]
    temp = max(max(row) for row in maze)
    start = []
    for x in range(n):
        for y in range(n):
            if maze[x][y]==temp:
                start.append((x,y))
    max_val = 0
    for x in range(len(start)):
        visited = [[0]*n for _ in range(n)]
        visited[start[x][0]][start[x][1]]=1
        backtrack(start[x][0],start[x][1],1,0)
    print(f'#{seq} {max_val}')