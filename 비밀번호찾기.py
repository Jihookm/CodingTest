import sys


n,m=map(int,sys.stdin.readline().split())
ans=dict()
for i in range(n):
    a,b=sys.stdin.readline().split()
    ans[a]=b
for i in range(m):
    c=sys.stdin.readline().rstrip()
    print(ans[c])