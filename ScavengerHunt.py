p,q=map(int,input().split())
temp=[]
temp2=[]
for i in range(1,p+1):
    if p%i==0:
        temp.append(i)
for i in range(1,q+1):
    if q%i==0:
        temp2.append(i)
for i in temp:
    for j in temp2:
        print(i,j)