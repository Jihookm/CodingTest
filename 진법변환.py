import sys
n,b=map(int,sys.stdin.readline().split())

temp='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=''
while n!=0:
    ans+=str(temp[n%b])
    n=n//b

print(ans[::-1])