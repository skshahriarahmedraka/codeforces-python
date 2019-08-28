n,a=list(map(int,input().split(" ")))
li=list(map(int,input().split(" ")))
li1=li[:a-1]
li2=li[a:]
li1.reverse()

i=0
j=0
ans=0
if li[a-1]==1:
    ans+=1
while i<len(li1) or j<len(li2):
    if i<len(li1) and j<len(li2):
        if li1[i]==1 and li2[j]==1:
            ans+=2
    elif i<len(li1) and j>=len(li2):
        if li1[i]==1:
            ans+=1
    else:
        if li2[j]==1:
            ans+=1
    i+=1
    j+=1
print(ans)
