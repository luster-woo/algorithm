def backtrack(cnt, num,idx,map):
    global max_val
    if cnt == m:
        max_val = max(max_val,num)
        return
    if idx == len(attack):
        return
    backtrack(cnt,num,idx+1,map)
    temp_map = [row[:] for row in map]
    result = 0
    x,y = attack[idx]
    if temp_map[x][y] > 0:
        dmg = min(temp_map[x][y], k)
        temp_map[x][y] -= dmg
        result += dmg
    for i in range(4):
        for j in range(1,k):
            ni = x+dx[i]*j
            nj = y+dy[i]*j
            pow = k-j
            temp  = 0
            if 0<=ni<n and 0<=nj<n and temp_map[ni][nj]==-1:
                break
            if 0<=ni<n and 0<=nj<n and temp_map[ni][nj]>0:
                if pow>temp_map[ni][nj]:
                    temp = temp_map[ni][nj]
                    temp_map[ni][nj]=0
                else:
                    temp = pow
                    temp_map[ni][nj]-=pow

            result += temp
    backtrack(cnt+1,num+result,idx+1,temp_map)




dx = [0,1,0,-1]
dy = [1,0,-1,0]
n = int(input())
for tc in range(1,n+1):
    n,m,k,c = map(int,input().split())
    maze = [list(map(int,input().split())) for _ in range(n)]
    attack = []
    for _ in range(c):
        a,b = map(int,input().split())
        attack.append((a,b))
    max_val = 0
    backtrack(0,0,0,maze)
    print(f'#{tc} {max_val}')