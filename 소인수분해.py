import sys
a=int(sys.stdin.readline().strip())

def fact(num):
    d=2 #하나씩 더해가면서 나눌 수
    while d<=num: #num보다 작은 d
        if num%d==0: #인수이면
            print(d)
            num=num//d #num을 d로 나눈 몫으로 바꿔줌
        else: #인수가 아니면
            d=d+1

fact(a)