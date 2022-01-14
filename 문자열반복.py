a=int(input())
arr=[]
srr=[]
ans=[]
for i in range(a):
    x,y=input().split()
    arr.append(int(x))
    srr.append(y)
    
for i in range(a):
    for j in range (len(srr[i])):
        for k in range(arr[i]):
            ans.append(srr[i][j])
    for j in range(len(ans)):
        print(ans[j],end='')
    print()
    ans.clear()

