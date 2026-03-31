import sys
input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def check():
    result_1 = not safe[8]
    result_2 = False
    for i in range(8):
        if valid[i] and safe[i]:
            result_2 = True
            break

    if result_1 and result_2: 
        return "CHECK"
    elif result_1 and not result_2:
        return "CHECKMATE"
    elif not result_1 and not result_2:
        return "STALEMATE"
    else:
        return "NONE"

n, k = map(int, input().split())
v1, v2 = map(int, input().split())
kx, ky = v1 - 1, v2 - 1

queens = []
for _ in range(k):
    temp1, temp2 = map(int, input().split())
    queens.append((temp1 - 1, temp2 - 1))

positions = [(0, 0)] * 9
valid = [False] * 9 
safe = [False] * 9  

for i in range(8):
    nx = kx + dx[i]
    ny = ky + dy[i]
    positions[i] = (nx, ny)
    if 0 <= nx < n and 0 <= ny < n:
        valid[i] = True
        safe[i] = True


positions[8] = (kx, ky)
valid[8] = True
safe[8] = True

for qx, qy in queens:
    for i in range(9):
        if not valid[i] or not safe[i]:
            continue
            
        px, py = positions[i]
        
        if qx == px and qy == py:
            continue
            
        if qx == px or qy == py or abs(qx - px) == abs(qy - py):
            safe[i] = False

print(check())