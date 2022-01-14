import sys
a=int(sys.stdin.readline())
arr=[]
for i in range(a):
    (x,y)=sys.stdin.readline().split()
    arr.append((int(x),y))

arr=sorted(arr,key=lambda x: x[0])
for i in range(a):
    print(arr[i][0],arr[i][1])
