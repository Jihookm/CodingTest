a,b=map(int,input().split())
nlist=set(map(int,input().split()))
n=set(map(int,input().split()))
print(len(nlist-n)+ len(n-nlist))