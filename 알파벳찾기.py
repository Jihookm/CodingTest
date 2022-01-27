import sys
word=sys.stdin.readline().strip()
alphabet=[-1]*26
for i in range(len(word),0,-1): #chr(숫자) : 해당 아스키코드, hex(숫자) : 헥사코드
    alphabet[ord(word[i-1])-97]=i-1 #ord(문자) : 아스키코드 번호 반환

for i in range(len(alphabet)-1):
    print(alphabet[i],end=' ')
print(alphabet[-1])