import heapq

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n)]
    result = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        result += c
    pq = [(0, 0)]
    visited = [0] * n
    edge_cnt = 0
    total_weight = 0
    while pq:
        cost, idx = heapq.heappop(pq)
        if visited[idx]:
            continue

        visited[idx] = 1
        total_weight += cost
        edge_cnt += 1

        if edge_cnt == n:
            break

        for nxt_idx, nxt_cost in graph[idx]:
            if not visited[nxt_idx]:
                heapq.heappush(pq, (nxt_cost, nxt_idx))

    print(result - total_weight)