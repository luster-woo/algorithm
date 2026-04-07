import heapq
T = int(input())
 
for tc in range(1,T+1):
    N = int(input())
    all_x = list(map(int, input().split()))
    all_y = list(map(int, input().split()))
    fee = float(input())
 
    visited = [0]*N
    min_edge = [float('inf')]*N
    min_edge[0] = 0
 
    hq = [(0, 0)]  # (cost, node)
    total = 0
    count = 0
 
    while hq:
        cost, node = heapq.heappop(hq)
 
        if visited[node]:
            continue
 
        visited[node] = 1
        count += 1
        total += cost
        if count == N:
            break
 
        for next_node in range(N):
            if not visited[next_node]:
                dist = (all_x[node]-all_x[next_node])**2 + (all_y[node]-all_y[next_node])**2
 
                if dist < min_edge[next_node]:
                    min_edge[next_node] = dist
                    heapq.heappush(hq, (dist, next_node))
                     
 
    print(f"#{tc} {int(total*fee+0.5)}")
