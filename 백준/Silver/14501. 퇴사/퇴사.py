import sys
input = sys.stdin.readline
def check(lev,cnt):
    global max_val
    if lev>n:
        return 
    if lev==n:
        max_val = max(max_val,cnt)
        return
    x,y = arr[lev]
    check(lev+x,cnt+y)
    check(lev+1,cnt)

n = int(input())
arr = []
max_val = 0 
for x in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
check(0,0)
print(max_val)