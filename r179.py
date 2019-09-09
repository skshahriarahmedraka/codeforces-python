n=int(input())

li=list(map(int,input().split(" ")))
fans=0
b=True
for i in range(len(li)):
    ans=0
    for j in range(len(li)):
        if not((abs(li[i]-li[j])%2)==0):
            ans+=1
            
    if b==True:
                fans=ans
                b=False
    if ans<fans:
        fans=ans
print(fans)