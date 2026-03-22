a,b = map(int,input().split())
for x in range(min(a,b),0,-1):
    if a%x==0 and b%x==0:
        print(x)
        break
for x in range(min(a,b),a*b+1,min(a,b)):
    if x%a==0 and x%b==0:
        print(x)
        break