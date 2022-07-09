import sys

N,M = map(int, sys.stdin.readline().split())
num = []
poke = []

for N in range(N):
  poke.append(sys.stdin.readline().rstrip())
  num.append(str(N+1))

poke_dic = dict(zip(num,poke))

for M in range(M):
  x=sys.stdin.readline().rstrip()
  if x in poke_dic.keys():
    print(poke_dic[x])
  else:
    y=poke.index(x)
    print(y+1)