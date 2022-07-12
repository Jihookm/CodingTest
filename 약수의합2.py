import sys
n = int(sys.stdin.readline())
s = 0
for i in range(1, n+1):
    s=s+ (n//i)*i

print(s)