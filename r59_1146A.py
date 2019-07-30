s=input()
x=0
y=0
for i in s:
    if(i== "a"):
        x+=1
    else:
        y+=1
if(x>y):
    print(x+y)
elif y>=x:
    print(x+x-1)