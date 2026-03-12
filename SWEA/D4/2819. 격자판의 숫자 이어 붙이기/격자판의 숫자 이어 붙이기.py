def dfs(x, y, number):
    if len(number) == 7:
        result.add(number)
        return
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = x + dx, y + dy
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, number + str(maze[ni][nj]))
num = int(input())
for seq in range(1,num+1):
    result = set()
    maze = [list(map(int,input().split())) for _ in range(4)]
    for x in range(4):
        for y in range(4):
            dfs(x,y,str(maze[x][y]))
    

    print(f'#{seq} {len(result)}')