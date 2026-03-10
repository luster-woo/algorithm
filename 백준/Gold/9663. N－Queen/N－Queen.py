def check(row):
    global cnt
    
    if row == n:
        cnt += 1
        return
    
    for col in range(n):
        path[row] = col
        
        for i in range(row):
            if path[i] == path[row] or abs(path[row]-path[i]) == row-i:
                break
        else:
            check(row+1)

n = int(input())
path = [0]*n
cnt = 0

check(0)
print(cnt)