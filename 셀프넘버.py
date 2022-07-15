nlist=set(range(1,10001))
temp=set()

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    temp.add(i)

ans=sorted(nlist - temp)
for i in ans:
    print(i)
