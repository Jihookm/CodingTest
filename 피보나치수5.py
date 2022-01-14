a=int(input())
arr=[0]*21
ans=1
arr[0]=0
arr[1]=1
for i in range(2,21):
    arr[i]=arr[i-1]+arr[i-2]
print(arr[a])