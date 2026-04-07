import heapq

def cnt(i, j):
    return ((x[i]-x[j])**2 + (y[i]-y[j])**2) * e

def prim():
    visited = [0]*n
    pq = [(0, 0)]
    total_cost = 0

    while pq:
        w, idx = heapq.heappop(pq)
        if visited[idx]:
            continue

        visited[idx] = 1
        total_cost += w

        for nxt_idx, nxt_w in graph[idx]:
            if not visited[nxt_idx]:
                heapq.heappush(pq, (nxt_w, nxt_idx))

    return total_cost

num = int(input())
for seq in range(1, num+1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            cost = cnt(i, j)
            graph[i].append((j, cost))
            graph[j].append((i, cost))

    print(f'#{seq} {round(prim())}')