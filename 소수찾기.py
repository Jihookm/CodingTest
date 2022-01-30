a=int(input())
arr=[]
arr=map(int, input().split())
arr=list(arr)
ans=0
for i in arr:
    if i !=1:
        temp=0
        for j in range(2,i):
            if i%j==0: #not
                temp+=1
        if temp==0:
            ans+=1
print(ans)
