import sys
import heapq
input = sys.stdin.readline

def dij(start, end):
    dist = [10**9] * (d+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        cost, idx = heapq.heappop(pq)
        
        if dist[idx] < cost:
            continue
        
        if idx >= end:
            return cost
        
        if idx + 1 <= d and dist[idx+1] > cost + 1:
            dist[idx+1] = cost + 1
            heapq.heappush(pq, (cost+1, idx+1))
        
        for next_idx, next_cost in graph[idx]:
            if next_idx <= d:
                new_cost = cost + next_cost
                if dist[next_idx] > new_cost:
                    dist[next_idx] = new_cost
                    heapq.heappush(pq, (new_cost, next_idx))
    
    return dist[end]

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= d:
        graph[a].append((b, c))

print(dij(0, d))