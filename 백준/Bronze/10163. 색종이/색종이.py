N = int(input())

x = []
y =[]
width = []
height = []
for a in range(N):
    xi,yi,wi,hi = list(map(int,input().split()))
    x.append(xi)
    y.append(yi)
    width.append(wi)
    height.append(hi)
result_1 =[]
for i in range(N):
    result = [[0]*1001 for _ in range(1001)]
    for p in range(x[i],x[i]+width[i]):
        for q in range(y[i],y[i]+height[i]):
            result[p][q]=1
    cnt = 0
    for a in range(i+1,N):
        for p in range(x[a],x[a]+width[a]):
            for q in range(y[a],y[a]+height[a]):
                result[p][q]=0
    for c in range(1001):
        for d in range(1001):
            if result[c][d]==1:
                cnt+=1
    result_1.append(cnt)
for i in range(len(result_1)):
    print(result_1[i])