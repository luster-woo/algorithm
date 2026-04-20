from collections import deque
tc = int(input())
def bfs(start):
    q = deque()
    q.append(start)
    visited[start]=1
    while q:
        x  = q.popleft()
        for nxt in graph[x]:
            if not visited[nxt]:
                visited[nxt]=1
                q.append(nxt)
    

for seq in range(1,tc+1):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(n+1)
    cnt = 0
    for x in range(1,n+1):
        if not visited[x]:
            bfs(x)
            cnt+=1
    print(f'#{seq} {cnt}')