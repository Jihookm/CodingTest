a=int(input())
temp=[0] * a
temp=map(int,input().split())
if sum(temp)%3 ==0:
    print('yes')
else:
    print('no')