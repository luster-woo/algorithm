from itertools import combinations

tc = int(input())
for seq in range(1, tc+1):
    n, m, c = map(int, input().split())
    bee = [list(map(int, input().split())) for _ in range(n)]
    
    arr = []
    

    for i in range(n):
        for j in range(n-m+1):
            segment = bee[i][j:j+m]
            
            best = 0
            for x in range(1, m+1):
                for comb in combinations(segment, x):
                    if sum(comb) <= c:
                        best = max(best, sum(v**2 for v in comb))
            
            arr.append((i, j, best))  
    
    max_val = 0
    
    for comb in combinations(arr, 2):
        (r1, c1, v1), (r2, c2, v2) = comb
        
        if r1 == r2 and not (c1 + m <= c2 or c2 + m <= c1):
            continue
        
        max_val = max(max_val, v1 + v2)
    
    print(f'#{seq} {max_val}')