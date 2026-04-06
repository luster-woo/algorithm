from collections import deque
def bfs(start):
    used[start]=cnt
    q = deque()
    q.append(start)
    while q:
        x= q.popleft()
        for nxt in graph[x]:
            if used[nxt]:
                continue
            used[nxt]=1
            q.append(nxt)
num = int(input())
for seq in range(1,num+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for x in range(0,len(arr),2):
        graph[arr[x]].append(arr[x+1])
        graph[arr[x+1]].append(arr[x])
    used= [0]*(n+1)
    cnt = 1
    for x in range(1,n+1):
        if used[x]:
            continue
        bfs(x)
        cnt+=1
    print(f'#{seq} {cnt-1}')
