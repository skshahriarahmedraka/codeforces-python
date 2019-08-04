n,k=input().split(" ")
n=int(n)
k=int(k)
s=input()
p1=0
p2=0
li=s.split(" ")
for i in range(n):
    li[i]=int(li[i])
    p1+=li[i]
for i in range(n-1):
    if li[i]+li[i+1]<k:
        p2+=k-li[i]-li[i+1]
        li[i+1]+=k-li[i]-li[i+1]
print(p2)
for i in range(n):
    print(str(li[i]), end=" ")
