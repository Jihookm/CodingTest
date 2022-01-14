import sys
a=int(sys.stdin.readline())
arr=[]
for i in range(a):
    arr.append(list(map(int,sys.stdin.readline().split())))
for i in range(a):
    arr[i][0],arr[i][1]=arr[i][1],arr[i][0]

arr=sorted(arr)
for i in range(a):
    print(arr[i][1],arr[i][0])
