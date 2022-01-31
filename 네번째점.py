#점 4개 배열에 저장
#x,y 각각 홀수번으로 나온 값이 네 번째 점의 좌표
x=[0]*4
y=[0]*4

for i in range(3):
    a, b=map(int, input().split())
    x[i]=a
    y[i]=b
for i in range(3):
    if x.count(x[i])==1:
        x[3]=x[i]
    if y.count(y[i])==1:
        y[3]=y[i]

print(x[3],y[3])