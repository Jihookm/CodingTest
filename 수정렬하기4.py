import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    a=int(sys.stdin.readline())
    arr.append(a)

arr.sort(reverse=True)
for i in arr:
    print(i)