import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

x, y = map(int, input().split())
INF = int(1e9)

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, now = heapq.heappop(pq)
        if dist[now] < cost:
            continue

        for nxt, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    return dist

d1 = dijkstra(1)
dx = dijkstra(x)
dy = dijkstra(y)

res1 = d1[x] + dx[y] + dy[n]
res2 = d1[y] + dy[x] + dx[n]

ans = min(res1, res2)

print(ans if ans < INF else -1)