T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [0] * (L+1)
    for score, cal in items:
        for j in range(L, cal-1, -1):  
            dp[j] = max(dp[j], dp[j-cal] + score)
    
    print(f"#{tc} {max(dp)}")