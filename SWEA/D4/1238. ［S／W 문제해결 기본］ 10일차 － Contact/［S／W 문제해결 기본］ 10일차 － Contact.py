from collections import deque
for tc in range(1,11):
    n,s = map(int,input().split())
    graph  = [[] for _ in range(101)]
    temp = list(map(int,input().split()))
    for x in range(0,n,2):
        graph[temp[x]].append(temp[x+1])
    q = deque()
    visited = [0]*101
    visited[s]=1
    q.append(s)
    while q:
        x= q.popleft()
        for idx in graph[x]:
            if not visited[idx]:
                q.append(idx)
                visited[idx]=visited[x]+1
    temp_idx = max(visited)
    arr = []
    for i in range(101):
        if visited[i]==temp_idx:
            arr.append(i)
    print(f'#{tc} {max(arr)}')