import heapq
import sys
input = sys.stdin.readline

min_hq = []
max_hq = []
problems = {}

n = int(input())
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(min_hq, (l, p))
    heapq.heappush(max_hq, (-l, -p))
    problems[p] = l

m = int(input())
for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'add':
        p, l = int(cmd[1]), int(cmd[2])
        heapq.heappush(min_hq, (l, p))
        heapq.heappush(max_hq, (-l, -p))
        problems[p] = l

    elif cmd[0] == 'solved':
        p = int(cmd[1])
        if p in problems:
            del problems[p]

    else: 
        if cmd[1] == '1':

            while True:
                l, p = max_hq[0]
                l, p = -l, -p
                if p in problems and problems[p] == l:
                    print(p)
                    break
                heapq.heappop(max_hq)

        else:
            while True:
                l, p = min_hq[0]
                if p in problems and problems[p] == l:
                    print(p)
                    break
                heapq.heappop(min_hq)