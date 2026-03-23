import sys
input = sys.stdin.readline
from itertools import combinations
def backtrack(comb):
    global min_val
    min_result = 0 
    for x,y in home:
        min_dist = 10**9
        for idx in range(len(comb)):
            length = abs(x-comb[idx][0])+abs(y-comb[idx][1])
            min_dist = min(min_dist,length)
        min_result+=min_dist
    min_val = min(min_val, min_result)



n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
home = []
chicken = []
min_val = 10**9
for x in range(n):
    for y in range(n):
        if maze[x][y]==1:
            home.append((x,y))
        elif maze[x][y]==2:
            chicken.append((x,y))
for comb in combinations(chicken,m):
    backtrack(comb)
print(min_val)