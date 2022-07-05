from math import factorial
n,k=map(int,input().split())

if k==0:
    print(1)
else:
    a=factorial(n)
    b=factorial(k)
    c=factorial(n-k)
    temp=int(a/(b*c))
    print(temp)