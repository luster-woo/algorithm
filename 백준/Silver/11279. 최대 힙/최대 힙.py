import sys
input = sys.stdin.readline
import heapq
n = int(input())
pq = []
for _ in range(n):
    temp  =int(input())
    if temp ==0:
        if pq:
            print(-1*heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq,-temp)
