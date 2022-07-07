from math import factorial


n=int(input())
temp=factorial(n)
temp=str(temp)
ans=0
for i in range(1,len(temp)+1):
    if temp[-i]=='0':
        ans=ans+1
    else:
        break

print(ans)