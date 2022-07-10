from operator import mod
import sys
a,b=map(int,sys.stdin.readline().split())
c,d=map(int,sys.stdin.readline().split())

def ans(a,b):
    while a%b!=0:
        m=a%b
        a=b
        b=m
    return b

temp=ans(a*d+b*c,b*d)
print((a*d+b*c)//temp,(b*d)//temp)