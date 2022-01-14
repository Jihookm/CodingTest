sum=0
arr=[]
arr=list(map(int,input().split()))
for i in range(len(arr)):
    sum+=arr[i]**2
print(sum%10)