import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

visited = [False] * (n+1)
pq = []
heapq.heappush(pq, (0, 1))

total = 0
max_edge = 0

while pq:
    cost, now = heapq.heappop(pq)
    
    if visited[now]:
        continue
    
    visited[now] = True
    total += cost
    max_edge = max(max_edge, cost)
    
    for next_cost, next_node in graph[now]:
        if not visited[next_node]:
            heapq.heappush(pq, (next_cost, next_node))

print(total - max_edge)