n=int(input())
a=int(input())
li=[]

for i in range(n):
    if  a%10==7 or a%10==3 or a%10==2 :
        li.append(a%10)
    elif a%10==9:
        li.append(2)
        li.append(3)
        li.append(3)
        li.append(7)
    elif a%10==8:
        li.append(2)
        li.append(2)
        li.append(2)
        li.append(7)
        
    elif a%10==6:
        li.append(3)
        li.append(5)
       
    elif a%10==5:
        li.append(5)
        
    elif a%10==4:
        li.append(2)
        li.append(2)
        li.append(3)
       
    elif a%10==3:
        li.append(3)
        
    elif a%10==2:
        li.append(2)
        
    a//=10
li.sort(reverse=True)

for i in range(len(li)):
    print(li[i],end="")