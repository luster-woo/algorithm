
from collections import deque
def topology(v):
    result = []
    q = deque()
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        curr = q.popleft()
        result.append(curr)
        for nxt in graph[curr]:
            indegree[nxt]-=1
            if indegree[nxt]==0:
                q.append(nxt)
    return result


for seq in range(1,11):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    indegree= [0]*(v+1)
    arr = list(map(int,input().split()))
    for x in range(0,len(arr),2):
        graph[arr[x]].append(arr[x+1])
        indegree[arr[x+1]]+=1
    result = topology(v)
    print(f'#{seq}', *result)