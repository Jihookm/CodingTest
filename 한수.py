import sys
n=sys.stdin.readline()
count=0
for i in range(1,int(n)+1):
    if len(str(i))<=2:
        count+=1
    else:
        a=str(i)
        for j in range(1,len(a)-1):
            temp=int(a[0])-int(a[1])
            t=1
            if int(a[j])-int(a[j+1]) ==temp:
                t+=1
        if t==len(a)-1:
            count+=1

print(count)