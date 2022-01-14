a=int(input())
studs=[]

for i in range(a):
    w, h=map(int, input().split())
    studs.append((w, h))

for i in studs:
    rank=1
    for j in studs:
        if i[0]<j[0] and i[1]<j[1]:
            rank=rank+1
    print(rank, end = " ")
	