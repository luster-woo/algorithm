import sys
input = sys.stdin.readline
import heapq
dx = [0,1,0,-1]
dy = [1,0,-1,0]
m,n = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]
pq = [(0,0,0)]

inf  = 10**9
graph = [[inf]*m for _ in range(n)]
graph[0][0]=0
while pq:
    cost,x,y = heapq.heappop(pq)
    if graph[x][y]<cost:
        continue
    for i in range(4):
        ni = x+dx[i]
        nj = y+dy[i]
        if 0<=ni<n and 0<=nj<m:
            new_cost = maze[ni][nj]+cost
            if graph[ni][nj]>new_cost:
                graph[ni][nj]=new_cost
                heapq.heappush(pq,(new_cost,ni,nj))
print(graph[n-1][m-1])
