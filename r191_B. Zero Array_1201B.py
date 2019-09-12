def func():
    n=int(input())
    li=list(map(int,input().split(" ")))
    ans=0
    for i in range(n):
        ans+=li[i]
    for i in range(n):
        if not (li[i]<=(ans-li[i])):
            print("NO")
            return

    if ans%2==0:
        print("YES")
    else:
        print("NO")
if __name__=="__main__":
    func()