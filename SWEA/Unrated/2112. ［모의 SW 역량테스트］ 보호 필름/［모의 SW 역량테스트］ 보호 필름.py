def check():
    for col in range(w):
        cnt = 1
        for row in range(1, d):
            if film[row][col] == film[row-1][col]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                break
        if cnt < k:
            return False
    return True

def backtrack(depth,cnt):
    global result
    if cnt>=result:
        return
    if check():
        result = cnt
        return

    if depth == d:
        return
    original = film[depth][:]
    backtrack(depth+1, cnt)
    film[depth] = [0]*w
    backtrack(depth+1, cnt+1)
    film[depth] = [1]*w
    backtrack(depth+1, cnt+1)
    film[depth] = original

tc = int(input())
for seq in range(1,tc+1):
    d,w,k = map(int,input().split())
    film = [list(map(int,input().split())) for _ in range(d)]
    result = 10**9
    if k==1:
        print(f'#{seq} 0')
    elif check():
        print(f'#{seq} 0')
    else:
        backtrack(0,0)
        print(f'#{seq} {result}')      