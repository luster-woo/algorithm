from itertools import combinations
def cnt(temp):
    result =0
    for comb in combinations(temp,2):
        result+=maze[comb[0]][comb[1]]
        result+=maze[comb[1]][comb[0]]
    return result
inf = 10**9
num = int(input())
for seq in range(1,num+1):
    n = int(input())
    maze = [list(map(int,input().split())) for _ in range(n)]
    min_val = inf
    for comb in combinations(range(n),n//2):
        temp = [i for i in range(n) if i not in comb]
        temp_1=cnt(comb)
        temp_2=cnt(temp)
        min_val = min(min_val,abs(temp_1-temp_2))
    print(f'#{seq} {min_val}')