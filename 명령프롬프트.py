a=int(input())
arr=[]
first=list(input())

for i in range(a-1):
    arr=list(input())
    for j in range(len(first)):
        if first[j]!=arr[j]:
            first[j]='?'
            
print(''.join(first))
