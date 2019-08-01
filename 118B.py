n= int(input())
for i in range(n+1):
    for j in range(n-i,0,-1):
        print(end="  ")
    for k in range(i+1):
        if(k==0):
            print(""+str(k),end="")
        else:
            print(" "+str(k),end="")
    for l in range(i,0,-1):
        print(" "+str(l-1),end="")
    print('')
for i in range(n-1,-1,-1):
    for j in range(n-i,0,-1):
        print(end="  ")
    for k in range(i+1):
        if(k==0):
            print(""+str(k),end="")
        else:
            print(" "+str(k),end="")
    for l in range(i-1,-1,-1):
        print(" "+str(l),end="")
    print('')
    
