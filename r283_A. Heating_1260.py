def main():
    t=int(input())
    for i in range(t):
        c,k=list(map(int,input().split(" ")))
        if k==1:
            print(k)
        elif c==1:
            print(k**2)
        elif c>k:
            print(k)
        else:
            x=int(k/c)
            li=[x for i in range(c)]
            y=k-c*x
            j=0
            while y>0:
                li[j]+=1
                y-=1
                j+=1
            sum=0
            for j in range(c):
                sum+=li[j]**2
            print(sum)
if __name__=="__main__":
    main()