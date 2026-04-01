import sys
input = sys.stdin.readline
from itertools import combinations
def attack(arr):
    erase = set()  
    for shot in arr:
        min_dist = d+1
        target_enemy = None
        for x, y in temp_1:
            if abs(x-n) > d:
                continue
            dist = abs(x-n) + abs(y-shot)
            if dist <= d:
                if dist < min_dist or (dist == min_dist and (target_enemy is None or y < target_enemy[1])):
                    min_dist = dist
                    target_enemy = (x, y)
        if target_enemy:
            erase.add(target_enemy)
    return erase

            
n,m,d = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
target = []
cnt = -1
for x in range(n):
    for y in range(m):
        if maze[x][y]==1:
            if cnt==-1:
                cnt = x
            target.append((x,y))
max_val = 0
length = len(target)
for comb in combinations(range(m),3):
    temp_1 = target[:]
    count = 0
    cnt_1 = cnt
    while temp_1 or cnt_1!=n:
        temp = attack(comb)
        temp_1= [t for t in temp_1 if t not in temp]
        cnt_1+=1
        count+=len(temp)
        temp_1 = [(x+1, y) for x, y in temp_1 if x+1<n]
    max_val = max(max_val, count)
print(max_val)


