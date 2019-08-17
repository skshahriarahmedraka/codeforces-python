n=int(input())
s=input()

li=s.split(" ")
for i in range(len(li)):
    li[i]=int(li[i])
li.sort(reverse=True)

a=li[0]
li2=[]
i=0
while i<n:
    if (a%li[i]==0) and (li[i] not  in li2):
            li2.append(li[i])
            del li[i]
            i-=1
            n-=1
    i+=1

print(li[0])
print(li2[0])
