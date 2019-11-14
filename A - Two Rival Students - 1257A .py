def main():
    t=int(input())
    for i in range(t):
        n,x,a1,b=list(map(int,input().split(" ")))
        a=max(a1,b)
        b=min(a1,b)
        if n-1 ==a-b:
            print(a-b)
            continue
        else:
            x1=a-b
            y1=x1+x
            if y1>(n-1):
                print(n-1)
                continue
            else:
                print(y1)




if __name__=="__main__":
    main()
