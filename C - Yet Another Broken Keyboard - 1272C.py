def main():
    a,b=[int(i) for i in input().split()]
    s=input()
    li=[i for i in input().split()]
    x=0
    ans=0
    bo=False
    
    for i in range(a):
        if s[i] in li:
            bo=True
            x+=1
        elif (s[i] not in li ) and bo:
            ans+=(x*(x+1)/2)
            x=0
            bo=False
        if i==(a-1):
            ans+=(x*(x+1)/2)
        
    print(int(ans))        
 
if __name__=="__main__":
    main()
