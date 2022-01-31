a=input()
ans=[]
for i in range(len(a)):
    ans.append(a[i])
    if i%10==9:
        ans.append(' ')
for i in range(len(ans)):
    if ans[i]==' ':
        print()
    else:
        print(ans[i],end='')
    