ans=0
for i in range(5):
    a=int(input())
    if a<40:
        ans=ans+40
    else:
        ans=ans+a
print(int(ans/5))