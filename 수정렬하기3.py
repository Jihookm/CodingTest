import sys
a=int(sys.stdin.readline())
arr=[0]*10001 #입력가능한 범위가 10000까지, 인덱스 활용
for i in range(a):
    arr[int(sys.stdin.readline())]+=1 #입력받을때마다 배열 원소 +1해주기

for i in range(10001):
    if arr[i]!=0:#뭔가 있으면
        for j in range(arr[i]):
            print(i)