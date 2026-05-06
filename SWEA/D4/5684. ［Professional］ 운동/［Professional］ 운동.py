import heapq

inf = 10**9

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        reverse_graph[b].append((a, c))

    ans = inf

    for start in range(1, n + 1):

        pq = [(0, start)]
        dist = [inf] * (n + 1)
        dist[start] = 0

        while pq:
            cost, idx = heapq.heappop(pq)

            if dist[idx] < cost:
                continue

            for nxt_idx, nxt_cost in graph[idx]:
                new_cost = cost + nxt_cost

                if dist[nxt_idx] > new_cost:
                    dist[nxt_idx] = new_cost
                    heapq.heappush(pq, (new_cost, nxt_idx))

        pq = [(0, start)]
        dist_1 = [inf] * (n + 1)
        dist_1[start] = 0

        while pq:
            cost, idx = heapq.heappop(pq)

            if dist_1[idx] < cost:
                continue

            for nxt_idx, nxt_cost in reverse_graph[idx]:
                new_cost = cost + nxt_cost

                if dist_1[nxt_idx] > new_cost:
                    dist_1[nxt_idx] = new_cost
                    heapq.heappush(pq, (new_cost, nxt_idx))

        for u in range(1, n + 1):
            if dist[u] == inf:
                continue

            for v, w in graph[u]:
                if dist_1[v] != inf:
                    ans = min(ans, dist[u] + w + dist_1[v])

    if ans == inf:
        ans = -1

    print(f"#{tc} {ans}")