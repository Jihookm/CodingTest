import sys
ans=set()
#ans list 대신 set을 사용하는게 중요함. 집합은!!
a=int(sys.stdin.readline())
for i in range(a):
    temp=sys.stdin.readline().strip().split()
    if len(temp)==1:
        if temp[0]=='all':
            ans=set([i for i in range(1,21)])
        else:
            ans=set()
    else:
        f,x=temp[0],temp[1]
        x=int(x)
        if f=='add':
            ans.add(x)
        elif f=='remove':
            if x in ans:
                ans.discard(x)
        elif f=='check':
            print(1 if x in ans else 0)
        elif f=='toggle':
            ans.discard(x) if x in ans else ans.add(x)