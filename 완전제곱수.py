a=int(input())
b=int(input())

c=0 #while문 내 변수
ans=0

#60~100이라면 1~59까지의 완전제곱수는 계산할 필요 없음
#불필요한 연산을 줄이기 위함
while 1:
    if c**2<a: #a와 b 사이의 최솟값 찾기
        c=c+1
    else:
        break
if c**2<=b: #최솟값이 a~b 사이에 존재하면
    m=c**2 #최솟값

    while 1:
        if c**2<=b: #c를 1씩 키워가며 완전제곱수 더하기
            ans=ans+c**2
            c=c+1
        else:
            break
    print(ans)
    print(m)
else:
    print(-1)