from collections import deque
def bfs(start, graph):
    visited = [False]*(n+1)
    q = deque([start])
    visited[start] = True
    count = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1
    return count

tc = int(input())
for seq in range(1, tc+1):
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        reverse_graph[b].append(a)

    answer = 0

    for i in range(1, n+1):
        bigger = bfs(i, graph)          
        smaller = bfs(i, reverse_graph) 
        if bigger + smaller == n-1:
            answer += 1

    print(f"#{seq} {answer}")