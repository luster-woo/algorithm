from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

num = int(input())
for seq in range(1,num+1):
    n,k = map(int,input().split())
    maze = [list(input().strip()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == "X":
                sx, sy = i, j
            elif maze[i][j] == "Y":
                ex, ey = i, j

    q = deque()
    visited = set()

    q.append((sx, sy, 0, 0, 3))  
    visited.add((sx, sy, 0, 3))

    ans = -1

    while q:
        x, y, cnt, length, d = q.popleft()

        if x == ex and y == ey:
            ans = length
            break

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            
            if (maze[nx][ny] == "G" or maze[nx][ny] == "Y"):
                state = (nx, ny, cnt, d)
                if state not in visited:
                    visited.add(state)
                    q.append((nx, ny, cnt, length+1, d))
            
            elif maze[nx][ny] == "T" and cnt < k:
                state = (nx, ny, cnt+1, d)
                if state not in visited:
                    visited.add(state)
                    q.append((nx, ny, cnt+1, length+1, d))

        nd = (d + 3) % 4
        state = (x, y, cnt, nd)
        if state not in visited:
            visited.add(state)
            q.append((x, y, cnt, length+1, nd))


        nd = (d + 1) % 4
        state = (x, y, cnt, nd)
        if state not in visited:
            visited.add(state)
            q.append((x, y, cnt, length+1, nd))

    print(f'#{seq} {ans}')