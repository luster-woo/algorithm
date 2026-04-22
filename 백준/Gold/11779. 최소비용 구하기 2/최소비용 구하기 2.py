import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
s,e = map(int,input().split())
pq = []
heapq.heappush(pq,(0,s))
inf = 10**9
dist = [inf]*(n+1)
dist[s]=0
parent = [-1] * (n+1)
while pq:
    cost,idx = heapq.heappop(pq)
    if dist[idx]<cost:
        continue
    for nxt_idx,nxt_cost in graph[idx]:
        new_cost = nxt_cost+cost
        if dist[nxt_idx]>new_cost:
            dist[nxt_idx]=new_cost
            parent[nxt_idx] = idx
            heapq.heappush(pq,(new_cost,nxt_idx))
path =[]
cur = e
while cur !=-1:
    path.append(cur)
    cur = parent[cur]
path.reverse()
print(dist[e])
print(len(path))
print(*path)