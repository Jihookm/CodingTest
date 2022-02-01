import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arrm=[]
arrp=[]
for i in range(len(arr)):
    if arr[i]<0:
        arrm.append(arr[i])
    else:
        arrp.append(arr[i])
arrm=set(arrm)
arrm=list(arrm)

arrp=set(arrp)
arrp=list(arrp)

arrm.sort()
arrp.sort()
for i in arrm:
    print(i, end=' ')
for i in arrp:
    print(i,end=' ')
