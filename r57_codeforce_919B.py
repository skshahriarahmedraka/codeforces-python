n=int(input())
x=1
i=0
while i<n:
    x=x+9
    y=x
    z=0
    while y>0:
        z=z+y%10
        y=y//10
    if z==10:
        i+=1
print(x)