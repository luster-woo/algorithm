from collections import deque

n, m = map(int, input().split())

move = {}
for _ in range(n):
    a, b = map(int, input().split())
    move[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    move[a] = b

visited = [False] * 101

q = deque()
q.append((1, 0))
visited[1] = True

while q:
    x, cnt = q.popleft()

    if x == 100:
        print(cnt)
        break

    for i in range(1, 7):
        nx = x + i
        if nx > 100:
            continue

        if nx in move:
            nx = move[nx]

        if not visited[nx]:
            visited[nx] = True
            q.append((nx, cnt + 1))