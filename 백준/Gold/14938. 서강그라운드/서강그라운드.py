import heapq
import sys
input = sys.stdin.readline
def dij(start):
    dist = [10**9] * (n+1)
    dist[start]=0
    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        now_cost,now_dist = heapq.heappop(pq)
        if dist[now_dist]<now_cost:
            continue
        for next_dist,next_cost in graph[now_dist]:
            new_cost = next_cost+now_cost
            if new_cost>m:
                continue
            elif dist[next_dist]>new_cost:
                dist[next_dist]=new_cost
                heapq.heappush(pq,(new_cost,next_dist))
    return dist
n,m,r = map(int,input().split())
val = [0]*(n+1)
temp = list(map(int,input().split()))
for x in range(1,n+1):
    val[x]=temp[x-1]
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
max_val =  0
for x in range(1,n+1):
    dist = dij(x)
    result = 0
    for y in range(len(dist)):
        if dist[y]!=10**9:
            result+=val[y]
    max_val = max(max_val,result)
print(max_val)
