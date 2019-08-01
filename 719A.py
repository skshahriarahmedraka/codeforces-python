import sys
n=int(input())
s=input()
li=[]
#li2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1]
#ans="UP"
li=s.split(" ")
for i in range(len(li)):
    li[i]=int(li[i])


if len(li)==1:
    if(li[0]==0):
        print("UP")
    elif (li[0]==15):
        print("DOWN")
    else:    
        print("-1")

elif li[len(li)-1]==0 :
    print("UP")
elif li[len(li)-1]==15:
    print("DOWN")
elif li[len(li)-1]-li[len(li)-2] ==-1 :
    print("DOWN")
else :
    print("UP")
#print(ans)
