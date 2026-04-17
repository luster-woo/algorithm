import sys
input = sys.stdin.readline
import heapq
def dij(starts, limit):
    dist = [10**9]*(v+1)
    pq = []

    for s in starts:
        dist[s] = 0
        pq.append((0,s))

    heapq.heapify(pq)

    while pq:
        cost, idx = heapq.heappop(pq)

        if cost > limit:   
            continue

        if dist[idx] < cost:
            continue

        for nxt, w in graph[idx]:
            new_cost = cost + w
            if new_cost > limit:  
                continue

            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    return dist
v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
temp_cnt, m_dist = map(int,input().split())
m_arr = list(map(int,input().split()))
temp_cnt, s_dist = map(int,input().split())
s_arr= list(map(int,input().split()))
result = 10**9
mac_dist = dij(m_arr, m_dist)
star_dist = dij(s_arr, s_dist)
blocked = [False] * (v+1)
for x in m_arr:
    blocked[x] = True
for x in s_arr:
    blocked[x] = True

for i in range(1, v+1):
    if blocked[i]:
        continue
    if mac_dist[i] > m_dist or star_dist[i] > s_dist:
        continue
    result = min(result, mac_dist[i] + star_dist[i])
print(result if result != 10**9 else -1)