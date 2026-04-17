import sys
input = sys.stdin.readline
import heapq
n = int(input())
m = int(input())
graph =[[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
total_cost = 0
total_edge = 0
pq= [(0,1)]
while pq:
    w,idx = heapq.heappop(pq)
    if visited[idx]:
        continue
    visited[idx]=1
    total_cost+=w
    total_edge+=1
    
    if total_edge == n:
        print(total_cost)
        exit()
    for nxt_idx,nxt_cost in graph[idx]:
        if not visited[nxt_idx]:
            heapq.heappush(pq,(nxt_cost,nxt_idx))
