
dx = [0,1,0,-1]
dy = [1,0,-1,0]

num = int(input())
for seq in range(1,num+1):
    n = int(input())
    maze = [list(input().strip()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == "X":
                sx, sy = i, j
            elif maze[i][j] == "Y":
                ex, ey = i, j
    dist = int(input())
    result = []
    for _ in range(dist):
        temp, temp_1 = map(str, input().split())
        idx = 3
        length = int(temp)
        arr = list(temp_1)
        a, b = sx, sy
        for x in arr:
            if x == "A":
                ni = a + dx[idx]
                nj = b + dy[idx]
                if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != "T":
                    a, b = ni, nj
            elif x == "L":
                idx = (idx + 3) % 4
            else:
                idx = (idx + 1) % 4
        if a==ex and b==ey:
            result.append(1)
        else:
            result.append(0)
    print(f'#{seq}',*result)