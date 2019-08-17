n=int(input())
z=0
for i in range(n):
    x,y=input().split(" ")
    x=int(x)
    y=int(y)
    if (x+y)>z:
        z=x+y
        ans=x+y
print(ans)
