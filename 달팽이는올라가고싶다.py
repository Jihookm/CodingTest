import sys
import math
a,b,v=map(int,sys.stdin.readline().split())
ans=(v-b)/(a-b) #마지막날 미끄러지는 경우 제외
print(math.ceil(ans))