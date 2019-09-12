def check(s):
    bal=0
    for i in range(len(s)):
        if s[i]=='(':
            bal+=1
        elif s[i]==")":
            bal-=1
        if bal<0:
            return False
    for i in range(len(s)-1,-1,-1):
        if s[i]=='(':
            bal+=1
        elif s[i]==")":
            bal-=1
        if bal>0:
            return False
    if bal ==0:
        return True
    else:
        return False
def check2(s):
    bal=0
    for i in range(len(s)):
        if s[i]=='(':
            bal+=1
        elif s[i]==")":
            bal-=1
        if bal<-1:
            return False
    for i in range(len(s)-1,-1,-1):
        if s[i]=='(':
            bal+=1
        elif s[i]==")":
            bal-=1
        if bal>1:
            return False
        
    if bal ==0:
        return True
    else:
        return False   
def func():
    n=int(input())
    s=input()
    if len(s)%2 !=0:
        print("No")
        return
    if check(s) and check2(s):
        print("Yes")
        return
    elif check2(s):
        print("Yes")
        return

    
    print("No") 
        
if __name__=="__main__":
    func()