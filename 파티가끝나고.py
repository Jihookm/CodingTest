a,b=map(int,input().split())
arr=[]
ans=[]
arr=list(map(int,input().split()))
for i in range(len(arr)):
    ans.append(arr[i]-a*b)
for i in range(len(ans)):
    print(ans[i],end=' ')
print()