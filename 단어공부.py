import sys
word=sys.stdin.readline().strip()
word=word.upper()
alphabet=[0]*26
for i in range(len(word)):
    alphabet[ord(word[i])-65]+=1
mal=max(alphabet)
ans=[]
for i in range(26):
    if alphabet[i]==mal:
        ans.append(i)

if len(ans)==1:
    print(chr(ans[0]+65))
else:
    print('?')
