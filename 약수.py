a=int(input())
af=[0]*a
af=map(int,input().split())
af=list(af)
af.sort()
print(af[0]*af[-1])