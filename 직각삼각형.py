ans=[]
while(1):
    a,b,c=map(int,input().split())
    if a==b==c==0 :
        break
    else:
        if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==c**2:
            ans.append('right')
        else:
            ans.append('wrong')

for i in range(len(ans)):
    print(ans[i])