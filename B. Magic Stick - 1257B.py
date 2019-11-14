def main():
    t=int(input())
    for i in range(t):
        a,b=list(map(int,input().split(" ")))
        a1=a
        bo=False
        while True:
            if bo :
                if a==a1 or a<=1:
                    print("NO")
                    break
                
            bo=True
            if b<=a:
                print("YES")
                break
            else:
                if a%2==0:
                    a=(3*a)/2
                else:
                    a-=1




if __name__=="__main__":
    main()
