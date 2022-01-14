a=input()
a=sorted(a,reverse=True)
for i in range(len(a)-1):
    print(a[i],end='')
print(a[-1])