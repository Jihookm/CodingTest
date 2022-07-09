n,m=map(int,input().split())
s=[]
ans=0
for i in range(n):
    s.append(input())
for i in range(m):
    if input() in s:
        ans=ans+1
        
print(ans)