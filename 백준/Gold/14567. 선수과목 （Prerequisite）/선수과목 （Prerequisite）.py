from collections import deque
n,m = map(int,input().split())
graph  = [[] for _ in range(n+1)]
degree = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b]+=1
result = [0]*(n+1)
q = deque()
for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)
        result[i]=1 
while q:
    x = q.popleft()
    
    for nxt in graph[x]:
        degree[nxt]-=1
        if degree[nxt]==0:
            result[nxt]=result[x]+1
            q.append(nxt)
result.pop(0)
print(*result)
