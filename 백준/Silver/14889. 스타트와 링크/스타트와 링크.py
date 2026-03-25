import sys
input = sys.stdin.readline
from itertools import combinations, permutations
n = int(input())
arr = [i for i in range(1,n+1)]
maze = [list(map(int,input().split())) for _ in range(n)]
min_val = 10**9
for comb in combinations(arr,n//2):
    arr_1 = [i for i in range(1,n+1) if i not in comb]
    result = 0 
    result_1 = 0
    for x,y in permutations(comb,2):
        result += maze[x-1][y-1]
    for x,y in permutations(arr_1,2):
        result_1 += maze[x-1][y-1]
    min_val = min(min_val,abs(result-result_1))
print(min_val)