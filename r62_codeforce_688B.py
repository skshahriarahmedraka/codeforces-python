'''n=int(input())
i=0
k=0
ans=0
def pal(i):
    r=0
    k=i
    for j,r in range(len(str(i))/2),range(len(str(i))/2,0,-1):

        
        
    if i==r:
        return True
    else :
        return False
while k<n:
    if len(str(i))%2==0:
        if pal(i):
            k+=1
            ans=i
    i+=1
print(ans)
'''
###############################
def fun(n):
    return n[::-1]
n=input()
n+=fun(n)
print(n)