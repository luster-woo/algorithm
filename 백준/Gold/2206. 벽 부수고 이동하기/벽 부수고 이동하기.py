from collections import deque
import sys
input = sys.stdin.readline

nx = [0,1,0,-1]
ny = [1,0,-1,0]

n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0,0,0))  # x, y, 벽쓴여부
    visited[0][0][0] = 1

    while q:
        x,y,wall = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for i in range(4):
            ni = x + nx[i]
            nj = y + ny[i]

            if 0<=ni<n and 0<=nj<m:
                # 길
                if maze[ni][nj] == 0 and visited[ni][nj][wall] == 0:
                    visited[ni][nj][wall] = visited[x][y][wall] + 1
                    q.append((ni,nj,wall))

                # 벽 (아직 안 부쉈으면)
                if maze[ni][nj] == 1 and wall == 0:
                    visited[ni][nj][1] = visited[x][y][0] + 1
                    q.append((ni,nj,1))

    return -1

print(bfs())