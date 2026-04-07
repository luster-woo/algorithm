dx = [0,1,0,-1]
dy = [1,0,-1,0]
import heapq
def dij():
    pq = [(0,0,0)]
    dist = [[10**9]*n for _ in range(n)]
    dist[0][0]=0
    while pq:
        cost,x,y = heapq.heappop(pq)
        if x == n-1 and y==n-1:
            return cost
        if dist[x][y]<cost:
            continue
        for i in range(4):
            ni = x+dx[i]
            nj = y+dy[i]
            if 0<=ni<n and 0<=nj<n:
                new_cost = cost+maze[ni][nj]
                if dist[ni][nj]>new_cost:
                    dist[ni][nj]=new_cost
                    heapq.heappush(pq,(new_cost,ni,nj))
    
num = int(input())
for seq in range(1,num+1):
    n = int(input())
    maze = [list(map(int,input().strip())) for _ in range(n)]
    print(f'#{seq} {dij()}')