from collections import deque
num = int(input())
for seq in range(1, num + 1):
    n, k = map(int, input().split())
    
    MAX = 1000000
    visited = [-1] * (MAX + 1)
    
    q = deque()
    q.append(n)
    visited[n] = 0

    while q:
        x = q.popleft()
        
        if x == k:
            print(f'#{seq} {visited[x]}')
            break

        for nx in (x*2, x+1, x-1, x-10):
            if 0 <= nx <= MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)