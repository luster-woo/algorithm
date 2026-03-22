n = int(input())
arr =list(map(int,input().split()))
result = 0
for x in arr:
    cnt = 0
    for div in range(1,x+1):
        if x%div==0:
            cnt+=1
        if cnt>=3:
            break
    if cnt==2:
        result+=1
print(result)