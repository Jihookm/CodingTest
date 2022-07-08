for i in range(3):
    temp=list(map(int,input().split()))
    if sum(temp)==0:
        print('D')
    elif sum(temp)==3:
        print('A')
    elif sum(temp)==2:
        print('B')
    elif sum(temp)==1:
        print('C')
    elif sum(temp)==4:
        print('E')