from math import factorial
n,k=map(int,input().split())
temp = [[1 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, k+1):
    for j in range(i+1, n+1):
        temp[j][i] = (temp[j-1][i-1] + temp[j-1][i]) % 10007

print(temp[n][k])