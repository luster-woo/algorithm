import heapq
inf = 10**9
def dij(s,graph):
    dist=[inf]*(n+1)
    dist[s]=0
    dist[0]=0
    pq = [(0,s)]
    while pq:
        cost,idx = heapq.heappop(pq)
        if dist[idx]<cost:
            continue
        for nxt_idx,nxt_cost in graph[idx]:
            new_cost = nxt_cost+cost
            if dist[nxt_idx]>new_cost:
                dist[nxt_idx]=new_cost
                heapq.heappush(pq,(new_cost,nxt_idx))
    return dist    
    

num = int(input())
for seq in range(1,num+1):
    n,m,x = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    graph_1 = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c =map(int,input().split())
        graph[a].append((b,c))
        graph_1[b].append((a,c))
    dist = dij(x,graph)
    dist_1 = dij(x,graph_1)
    max_val = 0
    for x in range(1,n+1):
        max_val = max(max_val,dist[x]+dist_1[x])
    print(f'#{seq} {max_val}')