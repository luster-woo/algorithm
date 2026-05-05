from collections import deque

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

tc = int(input())
for seq in range(1, tc+1):
    n = int(input())
    maze = [list(input().strip()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    count = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if maze[x][y] == '*':
                count[x][y] = -1  
            else:
                c = 0
                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if maze[nx][ny] == '*':
                            c += 1
                count[x][y] = c

    result = 0
    for x in range(n):
        for y in range(n):
            if count[x][y] == 0 and not visited[x][y]:
                result += 1
                q = deque()
                q.append((x,y))
                visited[x][y] = 1
                while q:
                    cx, cy = q.popleft()
                    for d in range(8):
                        nx = cx + dx[d]
                        ny = cy + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and count[nx][ny] != -1:
                                visited[nx][ny] = 1
                                if count[nx][ny] == 0:
                                    q.append((nx, ny))

    for x in range(n):
        for y in range(n):
            if count[x][y] > 0 and not visited[x][y]:
                result += 1

    print(f"#{seq} {result}")