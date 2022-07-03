n,m=map(int,input().split())
nlist=list(map(int,input().split()))
temp=[]
temp.append(0)
ans=[]
for i in nlist:
    temp.append(temp[-1]+i)
    
for _ in range(m):
    i,j=input().split()
    ans.append(temp[int(j)]-temp[int(i)-1])

for k in ans:
    print(k)