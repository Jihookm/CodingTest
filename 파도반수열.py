temp=[1,1,1,2,2]
t=int(input())
for i in range(95):
    temp.append(temp[i]+temp[i+4])
for i in range(t):
    n=int(input())
    print(temp[n-1])