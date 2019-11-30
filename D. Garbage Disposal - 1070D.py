from math import ceil,floor
def main():
    n,k=list(map(int,input().split(" ")))
    li=list(map(int,input().split(" ")))
    ans=0
    
    b=False
    for i in range(n):
        
        if i!=n-1:
            if li[i+1]==0:
                ans+=ceil(li[i]/k)
            elif b==True:
                ans+=ceil(li[i]/k)
                b=False
            else:
                if  ((li[i+1]+(li[i]%k))%k)>(li[i+1]):
                    b=True
                ans+=floor(li[i]/k)
                li[i+1]+=li[i]%k
        else:
            ans+=ceil(li[i]/k)
    print(ans)

if __name__=="__main__":
    main()
