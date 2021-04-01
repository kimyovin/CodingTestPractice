#myself
def caesarCipher(s, n):
    s = list(s)
    for i in range(len(s)) :
        hndln = 0
        if s[i] >= 'a':
            hndln = 97 
        elif s[i] >= 'A' and s[i]<='Z':
            hndln = 65
        if hndln != 0:
            s[i] = chr((ord(s[i])-hndln + n)%26 +hndln)
    s = ''.join(s)
    return ''.join(s)

  
'''

https://programmers.co.kr/learn/courses/30/lessons/12926
'''
