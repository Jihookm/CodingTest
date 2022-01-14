a=int(input())
arr=[0]*a
for i in range(a):
    arr[i]=int(input())
arr.sort()
for i in range(a):
    print(arr[i])