n=int(input())
s=input()
li=s.split(" ")
for i in range(n):
    li[i]=int(li[i])
x=0

y=-li[0]
if y<0:
    x=abs(y)
    y=y+x
for i in range(n-1):
    y=y+li[i]-li[i+1]
    if y<0:
        x=x+abs(y)
        y=y+abs(y)
    
print(x)