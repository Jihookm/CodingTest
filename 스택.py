import sys

s=[]

n=int(sys.stdin.readline())

for i in range(n):
    temp=sys.stdin.readline().split()
    if temp[0]=='push':
        s.append(temp[1])
    elif temp[0]=='top':
        if len(s)==0:
            print(-1)
        else:
            print(s[-1])
    elif temp[0]=='size':
        print(len(s))
    elif temp[0]=='empty':
        print(1 if len(s)==0 else 0)
    elif temp[0]=='pop':
        if len(s)==0:
            print(-1)
        else:
            print(s.pop(-1))