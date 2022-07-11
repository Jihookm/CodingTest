import sys
while 1:
    t=sys.stdin.readline().rstrip()
    if t=='END':
        break
    else:
        temp=[]
        for i in range(1,len(t)+1):
            temp.append(t[-i])
        for i in range(len(temp)-1):
            print(temp[i],end='')
        print(temp[-1])
