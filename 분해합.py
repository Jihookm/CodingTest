a=int(input())
tsum=0

for i in range(1,a+1):
    temp=list(map(int, str(i)))
    tsum=sum(temp)+i
    if tsum == a :
        print(i)
        break;
    if i==a :
        print(0)
