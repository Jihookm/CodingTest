n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    # 시간초과 - ans=(a**b)%10
    #거듭제곱 패턴 이용
    a_temp=a%10
    if a_temp==0:
        print(10)
    elif a_temp in [1,5,6]: #거듭제곱해도 일의자리수 동일
        print(a_temp)
    elif a_temp in [4,9]: #일의자리수 패턴 2개(4,6), (9,1)
        #b가 홀수면 a_temp 그대로, 아니면?
        if b%2==0:
            print((a_temp*a_temp)%10)
        else:
            print(a_temp)
    else: #패턴이 4개
        b_temp=b%4
        if b_temp==0:
            print(a_temp**4%10)
        else:
            print(a_temp**b_temp%10)