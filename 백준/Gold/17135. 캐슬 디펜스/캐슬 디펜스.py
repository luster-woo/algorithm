import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m, d = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0]   # 왼쪽, 위, 오른쪽
dy = [-1, 0, 1]

def bfs(col, board):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((n-1, col, 1))
    visited[n-1][col] = True

    while q:
        x, y, dist = q.popleft()

        if dist > d:
            return None

        if board[x][y] == 1:
            return (x, y)

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))

    return None


answer = 0

for comb in combinations(range(m), 3):
    board = [row[:] for row in origin]
    cnt = 0

    for _ in range(n):
        targets = set()

        # 공격 대상 찾기
        for col in comb:
            t = bfs(col, board)
            if t:
                targets.add(t)

        # 제거
        for x, y in targets:
            if board[x][y] == 1:
                board[x][y] = 0
                cnt += 1

        # 아래로 이동
        board.pop()
        board.insert(0, [0]*m)

    answer = max(answer, cnt)

print(answer)