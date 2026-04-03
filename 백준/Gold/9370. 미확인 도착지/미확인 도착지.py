import sys
import heapq
input = sys.stdin.readline

INF = 10**9

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        now_cost, now = heapq.heappop(pq)
        
        if dist[now] < now_cost:
            continue
        
        for next_node, weight in graph[now]:
            new_cost = now_cost + weight
            
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    
    return dist


tc = int(input())
for _ in range(tc):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    targets = [int(input()) for _ in range(t)]
    targets.sort()
    
    # 다익 3번
    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)
    
    # g-h 간선 길이 찾기
    gh_dist = INF
    for nxt, cost in graph[g]:
        if nxt == h:
            gh_dist = cost
            break
    
    result = []
    
    for x in targets:
        # s -> g -> h -> x
        path1 = dist_s[g] + gh_dist + dist_h[x]
        
        # s -> h -> g -> x
        path2 = dist_s[h] + gh_dist + dist_g[x]
        
        # 최단거리와 같으면 정답
        if dist_s[x] == path1 or dist_s[x] == path2:
            result.append(x)
    
    print(*result)