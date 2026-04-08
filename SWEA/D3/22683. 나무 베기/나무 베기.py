
from collections import deque


# 동, 남, 서, 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
for seq in range(1,T+1):
    n, k = map(int, input().split())
    maze = [list(input().strip()) for _ in range(n)]

    # 시작 / 끝 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'X':
                sx, sy = i, j
            elif maze[i][j] == 'Y':
                ex, ey = i, j

    # visited[x][y][dir][cnt]
    visited = [[[[0]*(k+1) for _ in range(4)] for _ in range(n)] for _ in range(n)]

    q = deque()

    # 시작: 북쪽(3)
    q.append((sx, sy, 3, 0, 0))  # x, y, dir, cnt, dist
    visited[sx][sy][3][0] = 1

    ans = -1

    while q:
        x, y, d, cnt, dist = q.popleft()

        # 도착
        if x == ex and y == ey:
            ans = dist
            break

        # 1. 전진
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            # 길 또는 도착
            if (maze[nx][ny] == 'G' or maze[nx][ny] == 'Y') and not visited[nx][ny][d][cnt]:
                visited[nx][ny][d][cnt] = 1
                q.append((nx, ny, d, cnt, dist+1))

            # 나무
            elif maze[nx][ny] == 'T' and cnt < k and not visited[nx][ny][d][cnt+1]:
                visited[nx][ny][d][cnt+1] = 1
                q.append((nx, ny, d, cnt+1, dist+1))

        # 2. 좌회전
        nd = (d + 3) % 4
        if not visited[x][y][nd][cnt]:
            visited[x][y][nd][cnt] = 1
            q.append((x, y, nd, cnt, dist+1))

        # 3. 우회전
        nd = (d + 1) % 4
        if not visited[x][y][nd][cnt]:
            visited[x][y][nd][cnt] = 1
            q.append((x, y, nd, cnt, dist+1))

    print(f'#{seq} {ans}')