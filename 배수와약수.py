import sys
ans=[]
while 1:
    a,b=map(int,sys.stdin.readline().split())
    if a==b==0:
        break
    elif b%a==0:
        ans.append('factor')
    elif a%b==0:
        ans.append('multiple')
    else:
        ans.append('neither')

for i in ans:
    print(i)

