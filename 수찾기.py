import sys

n=sys.stdin.readline()
nlist=set(map(int,sys.stdin.readline().split()))
m=sys.stdin.readline()
mlist=list(map(int,sys.stdin.readline().split()))

for i in mlist:
    print(1) if i in nlist else print(0)