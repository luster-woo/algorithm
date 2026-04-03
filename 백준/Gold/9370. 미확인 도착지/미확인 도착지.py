import heapq
import sys
input = sys.stdin.readline
import heapq

def dij(start):
    dist = [[10**9, 0] for _ in range(n+1)]
    dist[start] = [0, 0]
    pq = []
    heapq.heappush(pq, (0, start, 0))
    while pq:
        now_cost, now, now_idx = heapq.heappop(pq)
        if dist[now][0] < now_cost:
            continue
        for next_node, weight, idx in graph[now]:
            new_cost = now_cost + weight
            new_idx = now_idx + idx
            if new_cost < dist[next_node][0]:
                dist[next_node] = [new_cost, new_idx]
                heapq.heappush(pq, (new_cost, next_node, new_idx))
            elif new_cost == dist[next_node][0] and new_idx > dist[next_node][1]:
                dist[next_node] = [new_cost, new_idx]
                heapq.heappush(pq, (new_cost, next_node, new_idx))
    return dist
tc = int(input())
for _ in range(tc):
    n,m,t = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    s,g,h = map(int,input().split())
    for _ in range(m):
        v1,v2,cost = map(int,input().split())
        if (v1 == g and v2 == h) or (v1 == h and v2 == g):
            graph[v1].append((v2,cost,1))
            graph[v2].append((v1,cost,1))
        else:
            graph[v1].append((v2,cost,0))
            graph[v2].append((v1,cost,0))
    end = []

    for _ in range(t):
        temp  = int(input())
        end.append(temp)
    end.sort()
    dist = dij(s)
    for x in end:
        if dist[x][1]==1:
            print(x,end=" ")
    print()