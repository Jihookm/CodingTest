import sys
n=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
mlist=list(map(int,sys.stdin.readline().split()))

for i in range(m):
    if mlist[i] in nlist:
        mlist[i]=1
    else:
        mlist[i]=0

for i in mlist:
    print(i,end=' ')
print()