a,b=map(int,input().split())
c=int(input())

ans_a=a
ans_b=b+c
while ans_b>=60:
    ans_a=ans_a+1
    ans_b=ans_b-60

if ans_a>23:
    ans_a=ans_a-24

print(ans_a,ans_b)
