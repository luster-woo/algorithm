import heapq
def prim():
    visited=[0]*(v+1)
    pq =[(0,0)]
    total_cost = 0
    cnt = 0
    while pq:
        cost,idx = heapq.heappop(pq)
        if visited[idx]:
            continue
        visited[idx]=1
        total_cost +=cost
        cnt+=1
        if cnt==(v+1):
            return total_cost
        for nxt_idx,nxt_cost in graph[idx]:
            if not visited[nxt_idx]:
                heapq.heappush(pq,(nxt_cost,nxt_idx))

num = int(input())
for seq in range(1,num+1):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    print(f'#{seq} {prim()}')