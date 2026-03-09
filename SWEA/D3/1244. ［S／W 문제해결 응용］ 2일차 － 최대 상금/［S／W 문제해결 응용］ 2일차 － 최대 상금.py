def exchange(num, cnt):
    global result
    if cnt == b:
        result = max(result, int(''.join(num)))
        return
    state = (''.join(num), cnt)
    if state in visited:
        return
    visited.add(state)
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            exchange(num, cnt+1)
            num[i], num[j] = num[j], num[i]

n = int(input())

for seq in range(1,n+1):
    a, b = input().split()
    b = int(b)
    num = list(a)
    result = 0
    visited = set()
    exchange(num, 0)
    print(f'#{seq} {result}')