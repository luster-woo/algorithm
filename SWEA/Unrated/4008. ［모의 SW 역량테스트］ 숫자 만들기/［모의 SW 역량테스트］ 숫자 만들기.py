def backtrack(lev,val,p,m,mu,d):
    global max_val,min_val
    if lev==n:
        max_val = max(max_val,val)
        min_val = min(min_val,val)
        return
    if p>0:
        backtrack(lev+1,val+num_list[lev],p-1,m,mu,d)
    if m>0:
        backtrack(lev+1,val-num_list[lev],p,m-1,mu,d)   
    if mu>0:
        backtrack(lev+1,val*num_list[lev],p,m,mu-1,d)
    if d > 0:
        if val < 0:
            next_val = -(-val // num_list[lev])
        else:
            next_val = val // num_list[lev]
        backtrack(lev+1, next_val, p, m, mu, d-1)
num = int(input())
for seq in range(1,num+1):
    n = int(input())
    temp = list(map(int,input().split()))
    num_list = list(map(int,input().split()))
    min_val = 10**9
    max_val = -10**9
    backtrack(1,num_list[0],temp[0],temp[1],temp[2],temp[3])
    print(f'#{seq} {max_val-min_val}')
    