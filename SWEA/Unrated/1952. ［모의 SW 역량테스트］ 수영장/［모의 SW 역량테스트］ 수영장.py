tc = int(input())
def backtrack(lev,cnt):
    global min_val
    if lev==12:
        min_val = min(min_val,cnt)
        return 
    if cnt >= min_val:
        return
    if lev<9:
        backtrack(lev+3,cnt+price[2])
    else:
        backtrack(12,cnt+price[2])
    if month[lev]*price[0]>=price[1]:
        backtrack(lev+1,cnt+price[1])
    else:
        backtrack(lev+1,cnt+price[0]*month[lev])


for seq in range(1,tc+1):
    price = list(map(int,input().split()))
    month = list(map(int,input().split()))
    min_val = price[3]
    backtrack(0,0)
    print(f'#{seq} {min_val}')