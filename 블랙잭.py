a, b=map(int, input().split())
arr=[0] * a
ans=0
arr=map(int, input().split())
arr=list(arr)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            temp=arr[i]+arr[j]+arr[k] if arr[i]+arr[j]+arr[k] <=b else 0
            ans=ans if temp<ans else temp


print(ans)
