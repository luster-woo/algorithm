from itertools import combinations

n = int(input())
for _ in range(1,n+1):
    temp = int(input())
    dot = []
    for _ in range(temp):
        a,b = map(int,input().split())
        dot.append((a,b))
    max_val = 0
    for comb in combinations(dot, 3):
        xs = [p[0] for p in comb]
        ys = [p[1] for p in comb]
        if len(set(xs)) == 2 and len(set(ys)) == 2:
            width = max(xs) - min(xs)
            height = max(ys) - min(ys)
            max_val = max(max_val, width * height)
    print(max_val)