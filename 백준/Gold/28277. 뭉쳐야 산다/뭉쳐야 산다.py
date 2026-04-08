import sys
input = sys.stdin.readline
n,q = map(int,input().split())
arr = [set() for _ in range(n+1)]
for x in range(1,n+1):
    temp = list(map(int,input().split()))
    arr[x]=set(temp[1:])
for _ in range(q):
    temp = list(map(int,input().split()))
    if temp[0] == 1:
        a, b = temp[1], temp[2]

        if len(arr[a]) < len(arr[b]):
            arr[a], arr[b] = arr[b], arr[a]
        
        arr[a].update(arr[b])
        arr[b].clear()
    else:
        print(len(arr[temp[1]]))

