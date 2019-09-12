from copy import deepcopy
n=int(input())
li=list(map(int,input().split(" ")))
li2=deepcopy(li)
li2.sort()
x=len(li)

for i in range(1,x):
    li[i]+=li[i-1]
    li2[i]+=li2[i-1]
n2=int(input())
ans=[]

for i in range(n2):
    extra=list(map(int,input().split(" ")))
    if extra[0]==1:
        y=extra[1]-2
        if y<0:
            ans.append(li[extra[2]-1])
        else:
            ans.append(li[extra[2]-1]-li[y])
    else:
        y=extra[1]-2
        if y<0:
            ans.append(li2[extra[2]-1])
        else:
            ans.append(li2[extra[2]-1]-li2[y])

for i in range(n2):
    print(ans[i])
