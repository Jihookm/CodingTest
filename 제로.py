a=int(input())
arr=[]
for i in range(a):
    n=int(input())
    if n==0:
        arr.pop(-1)
    else:
        arr.append(n)
print(sum(arr))