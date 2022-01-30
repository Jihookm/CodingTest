import math
a,b=map(int,input().split())

def solve(n):
    arr=[1]*(n+1)
    arr[0],arr[1]=0,0 #0,1은 소수 아니니까 지워줌
    #개선된 알고리즘 : 2~ n의 제곱근까지 for문 돌리기
    #2~n까지의 수를 배열에 저장한 뒤 소수의 배수를 지움
    #2의 배수 다지우고 3의 배수, 5의 배수, 7,9...식으로
    #소수의 배수를 다 지우면 소수만 남음
    for i in range(2,int(math.sqrt(n)+1)):#가장 작은 소수 2부터
        if arr[i]==1:
            j=2 #몇 배수?
            while(i*j)<=n: #i*j가 n보다 작을 때
                arr[i*j]=0 #소수의 배수들을 0으로 지워줌
                j+=1
    return arr

arr=solve(b)

for i in range(a,len(arr)):
    if arr[i]==1: #소수이면
        print(i)
