def main():
    t=int(input())
    for i in range(t):
        a,b,c=[int(i) for i in input().split()]
        ans=0
        if a==b and b==c:
            print(ans)
            continue
        elif (a==b and abs(b-c)==1) or (b==c and abs(c-a)==1) or (a==c and abs(c-b)==1) :
            print(ans)
            continue
        elif a==b :
            ans=2 *(abs(b-c)-2)
            print(ans)
            continue
        elif b==c:
            ans=2 *(abs(b-a)-2)
            print(ans)
            continue
        elif a==c:
            ans=2 *(abs(b-c)-2)
            print(ans)
            continue
        else:
            ans=abs(a-b)+abs(b-c)+abs(c-a)-4
            print(ans)
 
 
 
if __name__=="__main__":
    main()
