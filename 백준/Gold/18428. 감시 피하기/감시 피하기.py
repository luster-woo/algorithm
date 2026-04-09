import sys
input = sys.stdin.readline 
from itertools import combinations
dx = [0,1,0,-1]
dy = [1,0,-1,0]
n = int(input())
maze = [list(map(str,input().split())) for _ in range(n)]
teachers = []
block = []
def check(maze):
    for tx,ty in teachers:
        for i in range(4):
            ni = tx+dx[i]
            nj = ty+dy[i]
            while 0<=ni<n and 0<=nj<n:
                if maze[ni][nj]=="O":
                    break
                elif maze[ni][nj]=="S":
                    return 
                ni+=dx[i]
                nj+=dy[i]
    print("YES")
    exit()
for x in range(n):
    for y in range(n):
        if maze[x][y]=="T":
            teachers.append((x,y))
        elif maze[x][y]=="X":
            block.append((x,y))
for comb in combinations(block,3):
    for x,y in comb:
        maze[x][y]="O"
    check(maze)
    for x,y in comb:
        maze[x][y]="X"
print("NO")
