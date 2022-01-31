a=list(input()) #일단 리스트로 저장
b=int(input())
#뒤에 두자리만 떼오기
#뒷자리를 00~ 가면서 전체 수가 b로 나눠지는지 확인
a_org=int("".join(a[0:-2]))

for i in range(100):
    temp=str(i)
    if i//10==0:
        temp='0'+str(i)

    if int(str(a_org)+temp)%b==0:
        print(temp)
        break
