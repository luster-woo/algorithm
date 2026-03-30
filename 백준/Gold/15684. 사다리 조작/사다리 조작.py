import sys
from itertools import combinations
input = sys.stdin.readline

def check():
    for start_node in range(n): 
        curr = start_node
        for row in range(1, h + 1):
            if ladder[row][curr]:
                curr += 1
            elif curr > 0 and ladder[row][curr-1]: 
                curr -= 1
        if curr != start_node:
            return False
    return True

def brute():
    for i in range(4):
        for comb in combinations(candidates, i):

            possible = True
            for k in range(len(comb)):
                for l in range(k + 1, len(comb)):
                    
                    if comb[k][0] == comb[l][0] and abs(comb[k][1] - comb[l][1]) == 1:
                        possible = False
                        break
                if not possible: break
            
            if not possible: continue

            for x, y in comb:
                ladder[x][y] = 1
            
            if check():
                print(i)
                exit()
                
            for x, y in comb:
                ladder[x][y] = 0
    print(-1)

n, m, h = map(int, input().split())
ladder = [[0] * (n + 1) for _ in range(h + 1)] 

for _ in range(m):
    a, b = map(int, input().split())
    ladder[a][b-1] = 1

candidates = []
for i in range(1, h + 1):
    for j in range(n - 1): 
        if not ladder[i][j]:
            if (j == 0 or not ladder[i][j-1]) and (not ladder[i][j+1]):
                candidates.append((i, j))

brute()