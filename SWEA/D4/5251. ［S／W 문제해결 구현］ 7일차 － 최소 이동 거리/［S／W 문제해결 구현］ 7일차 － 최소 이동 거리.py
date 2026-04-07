import heapq
inf = 10**9
def dij():
    dist= [inf] * (n+1)
    dist[0]=0
    pq = []
    heapq.heappush(pq,(0,0))
    while pq:
        cost,idx=  heapq.heappop(pq)
        if idx ==n:
            return dist[idx]
        if dist[idx]<cost:
            continue
        for nxt_idx,nxt_cost in graph[idx]:
            new_cost = nxt_cost+cost
            if new_cost<dist[nxt_idx]:
                dist[nxt_idx]=new_cost
                heapq.heappush(pq,(new_cost,nxt_idx))
    
num = int(input())
for seq in range(1,num+1):
    n,e = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
    print(f'#{seq} {dij()}')