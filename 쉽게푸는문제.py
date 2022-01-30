import sys
a,b=map(int,sys.stdin.readline().split())
ans=[]
sum=0
for i in range(46):
    for j in range(i+1):
        ans.append(i+1)

for k in range(a,b+1):
    sum+=ans[k-1]

print(sum)