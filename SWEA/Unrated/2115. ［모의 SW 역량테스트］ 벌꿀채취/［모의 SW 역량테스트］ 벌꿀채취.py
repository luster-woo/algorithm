from itertools import combinations

tc  = int(input())
for seq in range(1,tc+1):
    n,m,c = map(int,input().split())
    bee = [list(map(int,input().split())) for _ in range(n)]
    
    arr = []
    for i in range(n):
        for j in range(n-m+1):
            arr.append((i, j, bee[i][j:j+m])) 
    
    max_val = 0
    
    for comb in combinations(arr,2):
        (r1, c1, a1), (r2, c2, a2) = comb
        
        if r1 == r2 and not (c1 + m <= c2 or c2 + m <= c1):
            continue
        
        result = 0 
        
        if sum(a1) <= c:
            result += sum(i**2 for i in a1)
        else:
            temp_result = 0
            for x in range(1, m): 
                for comb_temp in combinations(a1, x):
                    if sum(comb_temp) <= c:
                        temp_result = max(temp_result, sum(i**2 for i in comb_temp))
            result += temp_result
        
        if sum(a2) <= c:
            result += sum(i**2 for i in a2)
        else:
            temp_result = 0
            for x in range(1, m):
                for comb_temp in combinations(a2, x):
                    if sum(comb_temp) <= c:
                        temp_result = max(temp_result, sum(i**2 for i in comb_temp))
            result += temp_result
        
        max_val = max(max_val, result)
    
    print(f'#{seq} {max_val}')