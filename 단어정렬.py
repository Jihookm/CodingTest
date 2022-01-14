import sys
a=int(sys.stdin.readline())
arr=[sys.stdin.readline().strip() for i in range(a)]
    
arr=list(set(arr))
arr=sorted(arr)
arr=sorted(arr, key=len)
arr=list(arr)
for i in range(len(arr)):
    print(arr[i])
