a=int(input())
ans=[]
for i in range(a):
    temp=input()
    count=0
    for j in temp:
        if j=='(':
            count=count+1
        else:
            count=count-1
            if count<0:
                break
    if count==0:
        ans.append('YES')
    else:
        ans.append('NO')

for i in ans:
    print(i)