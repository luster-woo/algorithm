import sys
input = sys.stdin.readline
from collections import deque
def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    union = [(x,y)]
    total = maze[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            ni = x + dx[i]
            nj = y + dy[i]

            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0:
                if l <= abs(maze[ni][nj] - maze[x][y]) <= h:
                    visited[ni][nj] = 1
                    q.append((ni,nj))
                    union.append((ni,nj))
                    total += maze[ni][nj]

    return union, total
n,l,h = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
day = 0

while True:
    visited = [[0]*n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                union, total = bfs(i,j)

                if len(union) > 1:
                    moved = True

                avg = total // len(union)

                for x, y in union:
                    maze[x][y] = avg

    if not moved:
        break

    day += 1
print(day)