n= int(input())
arr =list(map(int,input().split()))
div, div_1 = map(int,input().split())
cnt = 0
for x in arr:
    if x%div==0:
        cnt+=(x//div)
    else:
        cnt+=(x//div)+1
print(cnt)
print(n//div_1,n%div_1)