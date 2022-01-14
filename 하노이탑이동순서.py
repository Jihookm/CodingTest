import sys
from collections import Counter
a=int(sys.stdin.readline())


def hanoi(n, from_p, to_p, temp):
    if n==1:
        print(from_p, to_p)
        return
    hanoi(n-1,from_p,temp,to_p)
    print(from_p, to_p)
    hanoi(n-1,temp,to_p,from_p)
print(2**a-1)
hanoi(a,1,3,2)