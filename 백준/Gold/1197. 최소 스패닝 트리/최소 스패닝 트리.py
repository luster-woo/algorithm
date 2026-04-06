import sys
input = sys.stdin.readline
import heapq
def prim(start,v):
    visited = [0]*(v+1)
    pq = [(0,start)]
    total_cost = 0
    edge_count = 0
    while pq:
        w,idx = heapq.heappop(pq)
        if visited[idx]:
            continue
        visited[idx]=1
        total_cost+=w
        edge_count+=1
        if edge_count==v:
            return total_cost
        for nxt_node,nxt_w in graph[idx]:
            if not visited[nxt_node]:
                heapq.heappush(pq,(nxt_w,nxt_node))
        
v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
print(prim(1,v))
