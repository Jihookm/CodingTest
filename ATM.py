a=int(input())
b=list(map(int,input().split()))
b.sort()
ans=[0]*len(b)
ans[0]=b[0]
for i in range(1,len(b)):
    ans[i]=ans[i-1]+b[i]

print(sum(ans))