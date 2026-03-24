dx = [0,1,0,-1]
dy = [1,0,-1,0]
def can_connect(x, y, d):
    nx, ny = x, y
    path = []

    while True:
        nx += dx[d]
        ny += dy[d]

        if not (0 <= nx < n and 0 <= ny < n):
            return path  

        if board[nx][ny] != 0:
            return None  

        path.append((nx, ny))

def set_line(path, val):
    for x, y in path:
        board[x][y] = val

               
def backtrack(idx, cnt, length):
    global min_cnt, min_length
    if cnt + (len(process) - idx) < min_cnt:
        return

    if idx == len(process):
        if cnt > min_cnt:
            min_cnt = cnt
            min_length = length
        elif cnt == min_cnt:
            min_length = min(min_length, length)
        return
    x, y = process[idx]

    backtrack(idx+1, cnt, length)

    for d in range(4):
        path = can_connect(x, y, d)

        if path is None:
            continue

        set_line(path, 2)

        backtrack(idx+1, cnt+1, length + len(path))

        set_line(path, 0)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    process = []
    min_cnt = 0
    min_length = float('inf')
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i == 0 or j == 0 or i == n-1 or j == n-1:
                    continue
                process.append((i, j))
    backtrack(0, 0, 0)
    print(f'#{tc} {min_length}')