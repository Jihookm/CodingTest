a=int(input())
arr=[]
count=0
n=0
ans=[]
for i in range(a):
    arr=[]
    count=0
    n=0
    arr=list(map(int,input().split()))
    n=arr[0]
    arr.pop(0)
    average=sum(arr)/n
    for j in arr:
        if j>average:
            count=count+1
    ans.append((count/n)*100)
    
for i in range(a):
    print("{:.3f}%".format(ans[i]))