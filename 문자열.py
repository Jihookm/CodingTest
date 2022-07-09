a=int(input())
for i in range(a):
    temp=input()
    ans=[]
    ans.append(temp[0])
    ans.append(temp[-1])
    for j in ans:
        print(j,end='')
    print()