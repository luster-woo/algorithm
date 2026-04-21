from collections import deque

tc = int(input())
for seq in range(1, tc+1):
    n, k = map(int, input().split())

    arr = deque(input().strip())
    result = set() 
    for i in range(n//4):  
        for x in range(0, n, n//4):
            temp = ''.join(list(arr)[x:x+n//4])
            result.add(int(temp, 16))

        arr.appendleft(arr.pop())
    result = sorted(result, reverse=True)

    print(f"#{seq} {result[k-1]}")