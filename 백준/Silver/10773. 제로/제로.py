import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    temp = int(input())
    if temp ==0:
        arr.pop()
    else:
        arr.append(temp)
result = 0
for x in arr:
    result+=x
print(result)