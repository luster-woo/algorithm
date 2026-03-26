import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip())
stack = []
max_depth = 0
if n % 2 != 0:
    print(-1)
    exit()
for char in s:
    if stack and stack[-1] != char:
        stack.pop()
    else:
        stack.append(char)
    max_depth = max(max_depth, len(stack))
if stack:
    print(-1)
else:
    print(max_depth)