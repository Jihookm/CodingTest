n,m=map(int, input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
"""
if n>=m: #b에서 a로 옮기기
    for i in b:
        a.append(i)
    a.sort()
    for i in a:
        print(i, end=' ')
    print()
else:
    for i in a:
        b.append(i)
    b.sort()
    for i in b:
        print(i, end=' ')
    print()
"""

temp=[]
i=0;j=0
while 1:
    if i==n or j==m:
        break
    if a[i] <= b[j] :
        temp.append(a[i])
        i=i+1
    else:
        temp.append(b[j])
        j=j+1

if i<n:
    for k in range(i,n):
        temp.append(a[k])
elif j<m:
    for k in range(j,m):
        temp.append(b[k])

for k in temp:
    print(k, end=' ')
print()
