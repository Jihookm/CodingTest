import sys
from collections import Counter
a=int(sys.stdin.readline())
arr=[]
for i in range(a):
    arr.append(int(sys.stdin.readline()))
arr.sort()
arr_n = Counter(arr).most_common(2)

print(round(sum(arr)/a))
print(arr[a//2])
if len(arr_n)>1:
    if arr_n[0][1]==arr_n[1][1]:
        print(arr_n[1][0])
    else:
        print(arr_n[0][0])
else:
    print(arr_n[0][0])
print(arr[-1]-arr[0])