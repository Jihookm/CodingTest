c0=[1,0]
c1=[0,1]
a=int(input())

for i in range(a):
    num=int(input())

    if num==0:
        print("1 0")
    elif num==1:
        print("0 1")
    else:
        for j in range(2,num+1):
            c0.append(c0[j-1]+c0[j-2])
            c1.append(c1[j-1]+c1[j-2])
        print(f"{c0.pop()} {c1.pop()}")
        c0=[1,0]
        c1=[0,1]