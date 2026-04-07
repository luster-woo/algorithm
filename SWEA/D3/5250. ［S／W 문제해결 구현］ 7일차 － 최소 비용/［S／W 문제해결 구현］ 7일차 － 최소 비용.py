dx = [0,1,0,-1]
dy = [1,0,-1,0]
import heapq
def dij():
    dist = [[10**9]*n for _ in range(n)]
    dist[0][0]=0
    pq = []
    heapq.heappush(pq,(0,0,0))
    while pq:
        cost,x,y = heapq.heappop(pq)
        if dist[x][y]<cost:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                temp = maze[nx][ny] - maze[x][y]
                if temp > 0:
                    new_cost = cost + 1 + temp
                else:
                    new_cost = cost + 1
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    return dist[n-1][n-1]
num = int(input())
for seq in range(1,num+1):
    n = int(input())
    maze = [list(map(int,input().split())) for _ in range(n)]
    print(f'#{seq} {dij()}')
