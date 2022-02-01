import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

temp=arr.copy()
temp.sort()

ans=[]
for i in range(len(arr)):
    for j in range(len(temp)):
        if arr[i]==temp[j]:

            ans.append(j)
            temp[j]=-1
            arr[i]=-2

for i in ans:
    print(i,end=' ')