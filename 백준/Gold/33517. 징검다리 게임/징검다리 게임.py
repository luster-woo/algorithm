import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
memo = input().strip()

if 'J' not in memo:
    print("NO")
    exit()

total_A = memo.count('A')
has_D_total = 'D' in memo

for x in arr:
    if x > 0 and total_A == 0:
        print("NO")
        exit()
    if x == -1 and not has_D_total:
        print("NO")
        exit()


parts = memo.split('J')
M = len(parts) - 1 
segments = []

for i in range(M + 1):
    if i == M:
        s = parts[M] + parts[0]
    else:
        s = parts[i]
        
    a_cnt = s.count('A')
    

    safe = False
    idx_D = s.find('D')
    idx_A = s.find('A')
    
    if idx_D != -1 and (idx_A == -1 or idx_D < idx_A):
        safe = True
        
    segments.append((a_cnt, safe))

idx = 0

while idx < n - 1:
    next_val = arr[idx + 1]
    

    if idx == 0:
        seg_idx = 0
    else:
        seg_idx = (idx - 1) % M + 1
        
    a_cnt, safe = segments[seg_idx]

    if next_val > 0:
        if a_cnt < next_val:
            print("NO")
            exit()

    elif next_val == -1:
        if not safe:
            print("NO")
            exit()

    idx += 1

print("YES")