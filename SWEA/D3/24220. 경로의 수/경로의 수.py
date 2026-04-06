
def backtrack(idx,e):
    global cnt 
    if idx == e:
        cnt +=1
        return
    for x in graph[idx]:
        if not used[x]:
            used[x]=1
            backtrack(x,e)
            used[x]=0
num = int(input())
for seq in range(1,num+1):
    cnt = 0
    n,E = map(int,input().split())
    arr =list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for x in range(0,E*2,2):
        a = arr[x]
        b = arr[x+1]
        graph[a].append(b)
    s,e = map(int,input().split())
    used= [0]*(n+1)
    used[s]=1
    backtrack(s,e)
    print(f'#{seq} {cnt}')
