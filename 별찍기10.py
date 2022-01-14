import sys
from collections import Counter
a=int(sys.stdin.readline())
start=[[0 for i in range(a)] for i in range(a)]

def star(n):
    global start
    if n==3:
        start[0][:3]=[1]*3
        start[2][:3]=[1]*3
        start[1][:3]=[1,0,1]
        return
    div=n//3
    star(div)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(div):
                start[div*i+k][div*j:div*(j+1)]=start[k][:div]

star(a)

for i in start:
    for j in i :
        if j==1:
            print('*',end='')
        else:
            print(' ',end='')
    print()