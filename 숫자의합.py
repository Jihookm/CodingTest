import sys
a=int(sys.stdin.readline().strip())
sum=0
x=sys.stdin.readline().strip()
for i in range(len(x)):
    sum+=int(x[i])
print(sum)