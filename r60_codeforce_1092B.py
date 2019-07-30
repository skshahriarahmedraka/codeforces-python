n=int(input())
s=input()
li=s.split(" ")
for i in range(n):
    li[i]=int(li[i])
li.sort(reverse=True)
#print(li)
i=0
while i<n:
    if li[i]==li[i+1]:
        li[i]=0
        li[i+1]=0
        #n-=2
        #print(li)
    i+=2
    
x=0
i=0
while i<n:
    x=x+abs(li[i]-li[i+1])
    i+=2
print(x)