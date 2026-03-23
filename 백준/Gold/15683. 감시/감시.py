import sys
input = sys.stdin.readline
import copy
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dict = {1 :[[0],[1],[2],[3]], 2: [[0,2],[1,3]],3:[[0,1],[1,2],[2,3],[3,0]],4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],5:[[0,1,2,3]]}
def watch(x,y,dir,board):
        for d in dir:
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]
                if not (0 <= nx < n and 0 <= ny < m) or maze[nx][ny] == 6:
                    break
                if board[nx][ny] == 0:
                    board[nx][ny] = 7
def dfs(lev, board):
    global min_val
    if lev ==len(cctv):
        count = 0
        for x in range(n):
            for y in range(m):
                 if board[x][y]==0:
                      count+=1
        min_val = min(min_val,count)
        return
    x,y,idx = cctv[lev]
    for dir in dict[idx]:
        temp_board = copy.deepcopy(board)
        watch(x,y,dir,temp_board)
        dfs(lev+1,temp_board)

n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
cctv = []
min_val = 10**9
for x in range(n):
    for y in range(m):
        if 1<=maze[x][y]<=5:
            cctv.append((x,y,maze[x][y]))
dfs(0,maze)
print(min_val)