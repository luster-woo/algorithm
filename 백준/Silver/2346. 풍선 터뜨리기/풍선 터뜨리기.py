import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
temp = list(map(int,input().split()))

dq = deque()

for i in range(n):
    dq.append((i+1, temp[i]))

while dq:
    idx, move = dq.popleft()
    print(idx, end=' ')

    if not dq:
        break

    if move > 0:
        for _ in range(move-1):
            dq.append(dq.popleft())
    else:
        for _ in range(-move):
            dq.appendleft(dq.pop())