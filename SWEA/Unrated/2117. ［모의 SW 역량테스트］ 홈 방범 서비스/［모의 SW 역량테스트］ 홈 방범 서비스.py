tc = int(input())
for seq in range(1,tc+1):
    n,m = map(int,input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    result  = 0
    for i in range(n):
        for j in range(n):
            for r in range(1,2*n):
                cnt = 0
                for x in range(n):
                    for y in range(n):
                        if abs(x-i)+abs(y-j)<r:
                            if city[x][y]==1:
                                cnt+=1
                temp  = r*r+(r-1)*(r-1)
                if cnt*m>=temp:
                    result = max(cnt,result)
    print(f'#{seq} {result}')
                

