import sys
input = sys.stdin.readline
import heapq

inf = 10**9
n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    rev_graph[b].append((a, c))  

def dijkstra(start, graph):
    dist = [inf] * (n+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, now = heapq.heappop(pq)
        if dist[now] < cost:
            continue

        for nxt, w in graph[now]:
            new_cost = cost + w
            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    return dist


dist_from_x = dijkstra(x, graph)

dist_to_x = dijkstra(x, rev_graph)

answer = 0
for i in range(1, n+1):
    answer = max(answer, dist_from_x[i] + dist_to_x[i])

print(answer)