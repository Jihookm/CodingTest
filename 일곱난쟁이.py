temp=[0] * 9
for i in range(9):
    temp[i]=int(input())
ans=[]
a=sum(temp)-100
for i in range(8):
    for j in range(i+1,len(temp)):
        if temp[i]+temp[j]==a:
            ans.append(i)
            ans.append(j)
            break
temp[ans[0]]=0
temp[ans[1]]=0
temp.sort()
temp.pop(0)
temp.pop(0)

for i in temp:
    print(i)