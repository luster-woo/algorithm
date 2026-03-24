import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(q, visited, lev, cnt):

    if 7-lev+cnt < 4:
        return

    if lev == 7:
        if cnt >= 4:
            q_tuple = tuple(sorted(q, key=lambda t: (t[0], t[1])))
            temp.add(q_tuple)
        return

    q_list = list(q)
    for a, b in q_list:
        for i in range(4):
            ni = a + dx[i]
            nj = b + dy[i]
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
                bfs(q, visited, lev + 1, cnt + (1 if maze[ni][nj]=="S" else 0))
                visited[ni][nj] = 0
                q.pop()

maze = [list(input().strip()) for _ in range(5)]

temp = set()

for x in range(5):
    for y in range(5):
        visited = [[0]*5 for _ in range(5)]
        visited[x][y] = 1
        cnt = 1 if maze[x][y] == "S" else 0
        bfs(deque([(x, y)]), visited, 1, cnt)

print(len(temp))