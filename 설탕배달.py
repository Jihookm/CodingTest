import sys
a=int(sys.stdin.readline().strip())
ans=0
while a>=0:
    if a%5==0:#5의 배수면
        ans+=a//5
        print(ans)
        break
    a-=3
    ans+=1
else:
    print(-1)
