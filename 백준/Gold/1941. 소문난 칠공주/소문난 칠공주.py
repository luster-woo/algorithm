import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

arr = [list(input().strip()) for _ in range(5)]
coords = [(i, j) for i in range(5) for j in range(5)]

def is_connected(comb):
    q = deque([comb[0]])
    visited = set([comb[0]])
    comb_set = set(comb)

    while q:
        x, y = q.popleft()
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if (nx, ny) in comb_set and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))

    return len(visited) == 7

answer = 0

for comb in combinations(coords, 7):
    s_cnt = sum(1 for x, y in comb if arr[x][y] == 'S')
    if s_cnt < 4:
        continue


    if is_connected(comb):
        answer += 1

print(answer)