import sys
input = sys.stdin.readline
n = int(input())
n = bin(n)[2:]
cnt = 0
for x in n:
    if x == '1':
        cnt+=1
print(cnt)